import subprocess
import sys


print("Installing requirements...")
subprocess.run(
    [
        sys.executable,
        "-m",
        "pip",
        "install",
        "-r",
        "requirements.txt",
        "--disable-pip-version-check",
    ],
    check=True,
)

print("Installing Playwright Chromium...")
subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)

print("\nSetup complete! Run 'python main.py' to start MARK XLVIII.")
