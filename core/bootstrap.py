from __future__ import annotations

import importlib.metadata as metadata
import importlib.util
import subprocess
import sys
from pathlib import Path
from typing import Callable


_DIST_IMPORTS: dict[str, str] = {
    "beautifulsoup4": "bs4",
    "duckduckgo-search": "duckduckgo_search",
    "google-genai": "google.genai",
    "google-generativeai": "google.generativeai",
    "opencv-python": "cv2",
    "pillow": "PIL",
    "python-multipart": "multipart",
    "python-pptx": "pptx",
    "send2trash": "send2trash",
    "youtube-transcript-api": "youtube_transcript_api",
}


def _module_available(module: str) -> bool:
    return importlib.util.find_spec(module) is not None


def _requirement_available(requirement: str) -> bool:
    name = requirement.split(";", 1)[0].split("[", 1)[0].strip()
    if not name:
        return True
    try:
        metadata.version(name)
        return True
    except metadata.PackageNotFoundError:
        return _module_available(_DIST_IMPORTS.get(name.lower(), name.replace("-", "_")))


def _requirement_applies(requirement: str) -> bool:
    if ";" not in requirement:
        return True
    marker = requirement.split(";", 1)[1].strip()
    if marker == 'sys_platform == "win32"':
        return sys.platform == "win32"
    return True


def _read_requirements(path: Path) -> list[str]:
    if not path.exists():
        return []
    reqs: list[str] = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#") and not line.startswith("-"):
            if _requirement_applies(line):
                reqs.append(line)
    return reqs


def _playwright_browsers_ready() -> bool:
    result = subprocess.run(
        [sys.executable, "-m", "playwright", "install", "--dry-run", "chromium"],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0 and "Install browser" not in result.stdout


def ensure_runtime_requirements(log: Callable[[str], None] | None = None) -> None:
    if getattr(sys, "frozen", False):
        return

    base_dir = Path(__file__).resolve().parent.parent
    req_path = base_dir / "requirements.txt"
    requirements = _read_requirements(req_path)
    missing = [req for req in requirements if not _requirement_available(req)]
    if missing:
        if log:
            log(f"[Setup] Installing missing packages: {', '.join(missing)}")
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "-r",
                str(req_path),
                "--disable-pip-version-check",
            ],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            msg = (result.stderr or result.stdout or "Unknown pip error").strip()
            raise RuntimeError(f"Dependency install failed: {msg[:800]}")

    if _requirement_available("playwright") and not _playwright_browsers_ready():
        if log:
            log("[Setup] Installing Playwright Chromium browser...")
        subprocess.run(
            [sys.executable, "-m", "playwright", "install", "chromium"],
            check=True,
            capture_output=True,
            text=True,
        )
