from __future__ import annotations

import shutil
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
DIST = ROOT / "dist"
BUILD = ROOT / "build"
RELEASE = ROOT / "release"
EXE_NAME = "JARVIS_MARK_XLVIII_Setup"


def run(cmd: list[str]) -> None:
    print(" ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def ensure_pyinstaller() -> None:
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        run([sys.executable, "-m", "pip", "install", "pyinstaller", "--disable-pip-version-check"])


def clean() -> None:
    for path in (DIST, BUILD, RELEASE):
        if path.exists():
            shutil.rmtree(path)
    spec = ROOT / f"{EXE_NAME}.spec"
    if spec.exists():
        spec.unlink()
    RELEASE.mkdir(parents=True, exist_ok=True)


def build() -> None:
    sep = ";" if sys.platform == "win32" else ":"
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--noconfirm",
        "--clean",
        "--name",
        EXE_NAME,
        "--add-data",
        f"core/prompt.txt{sep}core",
        "--add-data",
        f"dashboard/static{sep}dashboard/static",
        "--hidden-import",
        "google.genai",
        "--hidden-import",
        "google.generativeai",
        "--hidden-import",
        "uvicorn.logging",
        "--hidden-import",
        "uvicorn.loops",
        "--hidden-import",
        "uvicorn.loops.auto",
        "--hidden-import",
        "uvicorn.protocols",
        "--hidden-import",
        "uvicorn.protocols.http",
        "--hidden-import",
        "uvicorn.protocols.http.auto",
        "--hidden-import",
        "uvicorn.protocols.websockets",
        "--hidden-import",
        "uvicorn.protocols.websockets.auto",
        "--hidden-import",
        "uvicorn.lifespan",
        "--hidden-import",
        "uvicorn.lifespan.on",
        "main.py",
    ]
    run(cmd)

    suffix = ".exe" if sys.platform == "win32" else ""
    built = DIST / f"{EXE_NAME}{suffix}"
    final = RELEASE / f"{EXE_NAME}{suffix}"
    shutil.copy2(built, final)
    print(f"\nFinal distribution ready: {final}")
    print("Share only the file in release/. Do not share the source folders.")


if __name__ == "__main__":
    ensure_pyinstaller()
    clean()
    build()
