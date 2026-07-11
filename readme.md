# MARK XLVIII (48)

## Cross-platform JARVIS-style personal AI assistant

**A FatihMakes Industries X Nox Industries build.**

Created with contributions from **MSX-Fury**.

MARK XLVIII is a real-time desktop AI assistant designed to hear, see, reason, remember, and control your computer through natural conversation. It combines Gemini Live audio, a PyQt6 tactical HUD, local system automation, screen and camera vision, persistent memory, web intelligence, file handling, and a remote phone dashboard into one assistant experience.

---

## Overview

MARK XLVIII is the next evolution of the MARK assistant line. It focuses on speed, reliability, and a more natural interaction loop: fast interrupt handling, immediate visual acknowledgements, parallel news search, automatic dependency setup, richer UI polish, cleaner desktop integration, and a source-free Windows distribution path.

The goal is simple: make the assistant feel less like a command runner and more like a practical operating layer for your computer.

---

## Detailed Features

### Voice and Conversation

- Real-time microphone input through Gemini Live.
- Low-latency assistant speech playback.
- Interrupt support with `Escape` and the in-app `INTERRUPT` button.
- Text command input for quiet use or debugging.
- Language-aware interaction behavior.
- Startup briefing flow for greetings, time, and news.
- Speaking/listening/thinking/processing visual states in the HUD.

### Desktop and System Control

- Launch local applications by voice or typed command.
- Control browser navigation, tabs, form input, and page interactions.
- Trigger keyboard shortcuts, typing, scrolling, mouse movement, and clicks.
- Manage volume, brightness, Wi-Fi, windows, fullscreen, refresh, lock, restart, and shutdown actions.
- Create desktop shortcuts without opening terminal windows.
- Run OS-native reminders through Windows Task Scheduler, macOS LaunchAgents, or Linux scheduling flows.

### Vision and Camera

- Analyze screenshots through the active AI session.
- Analyze webcam frames.
- Show a live camera feed inside the HUD.
- Show a smaller camera preview overlay for captured frames.
- Guard against repeated vision calls caused by echo or duplicate triggers.

### Web and Research

- Multi-mode web search: `search`, `news`, `research`, `price`, and `compare`.
- Parallel news lookup for faster and more reliable briefings.
- Weather reports.
- Flight search.
- YouTube search, playback, transcript, and metadata workflows.
- Dynamic content panel for showing web/news/search output inside the app.

### Files and Documents

- Drag-and-drop file upload zone.
- File type detection for images, video, audio, PDFs, Office files, code, archives, text, and data files.
- Summarize and answer questions about supported files.
- Local file operations through file controller tools.
- Desktop organization and file management actions.

### Development Tools

- Code explanation, generation, debugging, and review workflows.
- Developer task agent for larger coding jobs.
- Screenshot-aware support for UI/code debugging.
- Project file handling through local actions.

### Remote Dashboard

- Phone pairing through a temporary key.
- QR code pairing flow.
- Manual remote URL and key fallback.
- Dashboard command relay into the main assistant session.
- Optional phone microphone relay.

### Memory and Proactive Mode

- Persistent local memory for user preferences and identity context.
- Memory-aware prompts.
- Proactive check-ins after silence.
- Language preference retention.

### Distribution and Setup

- Automatic dependency bootstrap from `requirements.txt`.
- Playwright Chromium setup check.
- Manual setup script.
- Final source-free Windows `.exe` build path.
- First-run `.exe` install behavior with a Desktop shortcut.

---

## What's Added

| Addition | Details |
| --- | --- |
| Source-free Windows distribution | `build_final_exe.py` creates `release/JARVIS_MARK_XLVIII_Setup.exe`. |
| Desktop installer behavior | The frozen EXE copies itself to LocalAppData and creates a Desktop shortcut. |
| Automatic dependency bootstrap | `core/bootstrap.py` installs missing Python requirements before runtime imports. |
| PyQt6 dependency tracking | `PyQt6` is now included in `requirements.txt`. |
| Modern UI polish | Cards, popups, inputs, buttons, and panels use a cleaner modern design system. |
| Amber hologram HUD mode | The fallback center HUD now uses amber holographic particles, arcs, trails, and glow. |
| Collaboration branding | App title/footer and README show `FatihMakes Industries X Nox Industries`. |
| Contributor recognition | MSX-Fury is listed with separate social links. |
| Professional README | The README now includes setup, distribution, security, troubleshooting, and release notes. |

---

## What's Fixed

| Fix | Impact |
| --- | --- |
| Missing packages on launch | The app checks and installs required Python packages before importing runtime modules. |
| Missing UI package | `PyQt6` is included so the HUD can install and run correctly. |
| Playwright setup friction | Chromium can be installed automatically when needed. |
| Desktop distribution complexity | Users can run one EXE instead of dealing with source files. |
| Old branding mismatch | The UI no longer shows the old Stark footer branding. |
| Flat center HUD | The center HUD was redesigned into a more realistic amber hologram. |
| Center text clutter | The fallback HUD no longer writes `J.A.R.V.I.S` in the center of the hologram. |
| Blue/cyan ring conflict | The fallback amber HUD suppresses the old blue side arc style. |
| Popup/card sharpness | Buttons, inputs, cards, overlays, and panels now use softer rounded geometry. |
| Vision/session carryover | Transient vision and interrupt flags reset between sessions. |
| Slow interrupt UX | The interrupt command is clearly exposed through the UI and keyboard shortcut. |

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/FatihMakes/Mark-XLVIII.git
cd Mark-XLVIII
```

### 2. Run the app

```bash
python main.py
```

On first launch, MARK XLVIII automatically installs missing Python packages from `requirements.txt`. If Playwright Chromium is missing, it is installed as a one-time setup step.

### Optional manual setup

```bash
python setup.py
python main.py
```

---

## Final Windows Distribution

To build a source-free Windows distribution, run:

```bash
python build_final_exe.py
```

The final shareable file is created here:

```text
release/JARVIS_MARK_XLVIII_Setup.exe
```

Give users only the `.exe` inside `release/`. Do not share the source folders.

When the user opens the EXE, it installs JARVIS into the local app data folder, creates a Desktop shortcut, and launches the installed app. After that, the user can open JARVIS anytime from the Desktop shortcut.

---

## Requirements

| Requirement | Details |
| --- | --- |
| Operating system | Windows 10/11, macOS, or Linux |
| Python | Python 3.11 or 3.12 recommended for source runs |
| Microphone | Required for voice interaction |
| Internet | Required for Gemini Live, web search, setup, and cloud-backed features |
| Gemini API key | Required on first launch |
| Webcam | Optional, used for camera vision |

---

## Configuration

On first launch, the setup overlay asks for:

- Gemini API key
- Operating system selection

The app stores configuration in:

```text
config/api_keys.json
```

Do not commit your personal API keys to a public repository.

---

## Project Structure

```text
Mark-XLVIII/
|-- main.py                  # Main runtime loop, Gemini Live session, audio, tool dispatch
|-- ui.py                    # PyQt6 desktop HUD and interaction surface
|-- setup.py                 # Manual dependency setup helper
|-- requirements.txt         # Python runtime dependencies
|-- build_final_exe.py       # Source-free Windows EXE builder
|-- actions/                 # Tool implementations for desktop, browser, files, web, games, etc.
|-- config/                  # Local API keys and runtime configuration
|-- core/
|   |-- bootstrap.py         # Automatic dependency bootstrap used before runtime imports
|   |-- desktop_install.py   # Frozen EXE install and Desktop shortcut behavior
|   |-- installer.py         # Dependency installer helpers for configured engines
|   |-- llm_client.py        # LLM client utilities
|   |-- prompt.txt           # JARVIS behavior and tool routing prompt
|   |-- stt.py               # Speech-to-text support
|   `-- tts.py               # Text-to-speech support
|-- dashboard/               # Phone remote dashboard server and static client
`-- memory/                  # Persistent memory storage
```

---

## Important Files

| File | Purpose |
| --- | --- |
| `main.py` | Starts the app, connects to Gemini Live, dispatches tools, runs background tasks. |
| `ui.py` | Contains the desktop HUD, overlays, popups, buttons, panels, logs, and hologram renderer. |
| `core/bootstrap.py` | Checks and installs missing dependencies automatically before app imports. |
| `core/desktop_install.py` | Handles first-run install behavior for the frozen Windows EXE. |
| `build_final_exe.py` | Builds the final shareable setup EXE. |
| `requirements.txt` | Source of truth for required Python packages. |
| `dashboard/server.py` | Runs the optional phone remote dashboard. |
| `actions/` | Houses individual tools such as browser control, reminders, screen processing, file tools, and search. |

---

## Contributors

| Contributor | Role |
| --- | --- |
| FatihMakes | Creator and project lead |
| MSX-Fury | Contributor |

---

## Contributor Socials

| Contributor | Platform | Handle |
| --- | --- | --- |
| MSX-Fury | Instagram | [@thecyberhax](https://www.instagram.com/thecyberhax) |
| MSX-Fury | Discord | [Join Our Discord!](https://discord.gg/6ANGxWGaBk) |
| MSX-Fury | GitHub | [@msxfury](https://github.com/msxfury) |

---

## Security Notes

- API keys are stored locally under `config/`.
- Remote dashboard pairing uses a temporary key flow.
- Some actions can control your computer. Review commands and run the project only from a trusted local environment.
- Do not publish personal `config/api_keys.json` files.

---

## Troubleshooting

### Missing packages

Run:

```bash
python main.py
```

The app should install missing packages automatically. If pip fails, run:

```bash
python setup.py
```

### Playwright browser missing

Run:

```bash
python -m playwright install chromium
```

### Microphone problems

Check your operating system privacy settings and make sure the selected Python interpreter has microphone access.

### API key problems

Delete or edit:

```text
config/api_keys.json
```

Then restart the app to open the setup overlay again.

---

## Roadmap Ideas

- More polished remote dashboard workflows.
- Expanded local model support.
- Better plugin-style tool registration.
- More structured memory editing.
- Installer UX with visible progress inside the desktop app.

---

## License

Personal and non-commercial use only.
Licensed under **[Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**.

---

## Connect with the Creator

Engineered by a developer building a real-world JARVIS-style assistant.
**Star the repository to support the journey to Mark 100.**

| Platform | Link |
| --- | --- |
| Instagram | [@fatihmakes](https://www.instagram.com/fatihmakes) |
