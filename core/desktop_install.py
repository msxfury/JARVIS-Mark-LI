from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


APP_VENDOR = "FatihMakes Industries X Nox Industries"
APP_NAME = "MARK XLVIII"
EXE_NAME = "JARVIS MARK XLVIII.exe"
SHORTCUT_NAME = "JARVIS MARK XLVIII.lnk"


def _install_dir() -> Path:
    root = os.environ.get("LOCALAPPDATA") or str(Path.home() / "AppData" / "Local")
    return Path(root) / APP_VENDOR / APP_NAME


def _desktop_dir() -> Path:
    try:
        import ctypes
        from ctypes import wintypes

        buf = ctypes.create_unicode_buffer(wintypes.MAX_PATH)
        ctypes.windll.shell32.SHGetFolderPathW(None, 0x0000, None, 0, buf)
        if buf.value:
            return Path(buf.value)
    except Exception:
        pass
    return Path.home() / "Desktop"


def _create_shortcut(target: Path, shortcut: Path) -> None:
    shortcut.parent.mkdir(parents=True, exist_ok=True)
    vbs = "\n".join(
        [
            'Set ws = CreateObject("WScript.Shell")',
            f'Set sc = ws.CreateShortcut("{shortcut}")',
            f'sc.TargetPath = "{target}"',
            f'sc.WorkingDirectory = "{target.parent}"',
            'sc.Description = "J.A.R.V.I.S MARK XLVIII"',
            f'sc.IconLocation = "{target},0"',
            "sc.Save",
        ]
    )
    fd, tmp = tempfile.mkstemp(suffix=".vbs")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(vbs)
        flags = 0
        if hasattr(subprocess, "CREATE_NO_WINDOW"):
            flags |= subprocess.CREATE_NO_WINDOW
        subprocess.run(["wscript.exe", "/nologo", tmp], creationflags=flags, check=False)
    finally:
        try:
            os.unlink(tmp)
        except OSError:
            pass


def ensure_desktop_install() -> None:
    """
    For the frozen Windows build, install the single EXE into LocalAppData and
    create a Desktop shortcut. Source launches and non-Windows platforms are left alone.
    """
    if not getattr(sys, "frozen", False) or sys.platform != "win32":
        return

    current = Path(sys.executable).resolve()
    install_dir = _install_dir()
    target = install_dir / EXE_NAME

    if current != target.resolve():
        install_dir.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy2(current, target)
        except shutil.SameFileError:
            pass
        _create_shortcut(target, _desktop_dir() / SHORTCUT_NAME)

        env = os.environ.copy()
        env["JARVIS_INSTALLED_RUN"] = "1"
        subprocess.Popen([str(target)], cwd=str(install_dir), env=env)
        raise SystemExit

    _create_shortcut(target, _desktop_dir() / SHORTCUT_NAME)
