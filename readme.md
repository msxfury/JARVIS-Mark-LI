# ⚙️ MARK LI (51)
### The Ultimate Cross-Platform Personal AI Assistant — Maintained by msxfury

> 📺 **[Watch the full setup video on YouTube](https://www.youtube.com/@FatihMakes)**

A real-time voice AI that can hear, see, understand, and control your computer — on any OS. Supports Windows, macOS, and Linux. Built on the Gemini Live API for native audio streaming, delivering zero subscriptions and total digital autonomy.

---

## ✨ Overview

MARK LI is the final form of the core: an assistant you extend without ever touching its engine. Drop a single plugin file into the `plugins/` folder and JARVIS learns a new skill on the next launch — no code changes, no configuration, no risk. On top of that, the voice itself got smarter: JARVIS now hears the emotion in your voice, knows when you're talking to someone else in the room and stays silent, and can hold one conversation for hours without losing the thread.

It's not just an assistant — it's an extension of your digital life.

---

## 🚀 Capabilities

### Core Features
| Feature | Description |
|---|---|
| 🧩 Plugin System | Drop a single `.py` file into `plugins/` — JARVIS learns a new skill on next launch |
| 🎙️ Real-time Voice | Ultra-low latency conversation in any language via Gemini Live API |
| 💓 Affective Dialog | Hears the emotion in your voice and adapts its tone in response |
| 🤫 Proactive Audio | Knows when you're not talking to it — background chatter never triggers a reply |
| ♾️ Unlimited Sessions | Sliding-window context compression — one conversation can last for hours |
| 🖥️ System Control | Launch apps, adjust volume/brightness, WiFi, shortcuts, power — all by voice |
| 🧩 Autonomous Tasks | High-level planning for complex multi-step goals via agent mode |
| 👁️ Visual Awareness | Real-time screen capture and webcam vision piped into your main Gemini session |
| 🧠 Persistent Memory | Deeply remembers projects, preferences, and personal context across sessions |
| ⌨️ Hybrid Input | Seamlessly switch between keyboard typing and voice commands |
| 🌅 Morning Briefing | On first boot: greets you, reads the time, recaps yesterday, and fetches live news |
| 🔔 Proactive 2.0 | Time-aware, context-aware check-ins — knows the time of day, your projects, and what you've been discussing |
| 🗓️ Session Memory | Summarises each conversation and mentions it naturally next morning — consumed after use, never repeats |
| 👁️‍🗨️ Background Monitoring | User-configured topic watching — checks for new headlines once a day and alerts naturally |
| 📊 Hardware Monitoring | Continuous CPU, RAM, GPU and temperature telemetry with localized voice alerts |
| 🌤️ Weather Report | Live weather data for your city, personalized from memory |
| 🗺️ Dynamic Content Panel | Scrollable display layer beneath the HUD that renders web results, news, and search data |
| 🔍 Multi-Mode Web Search | `news` / `research` / `price` / `compare` / `search` — Gemini Grounded first, DDG fallback |
| ⏰ Smart Reminders | OS-native scheduled notifications (Windows Task Scheduler / macOS LaunchAgent / Linux systemd) |
| ✈️ Flight Finder | Live flight price and availability lookup |
| 🎮 Game Updater | Checks and triggers game updates on Steam and Epic Games on demand |
| 📂 File Processor | Read, summarize, and answer questions about local files |
| 💻 Code Helper | Inline code review, debugging, and generation |
| 🌐 Browser Control | Open URLs, navigate tabs, and interact with the browser by voice |
| 📨 Send Message | Compose and send messages through WhatsApp, Telegram, and more |
| 🎬 YouTube Control | Search, play, and control YouTube playback by voice |
| 🖱️ Desktop Control | Taskbar, window management, and desktop-level operations |
| 🧑‍💻 Silent Language Memory | Detects spoken language on first use — all future sessions adapt automatically |
| 📱 Remote Dashboard | Control the assistant from your phone via QR code pairing |
| ⚡ Auto-Start on Boot | Registers with the OS startup system (registry / LaunchAgent / .desktop) |
| 📋 Clipboard Intelligence | Copy any text → floating panel with Translate / Summarise / Explain / Fix |
| 🎨 Assistant Customization | Change the assistant name and your name from the UI — takes effect immediately |

---

## 🆕 What's New in Mark LI

### 🧩 Plugin System — Extend JARVIS Without Touching a Single Core File
The headline feature of Mark LI, and the reason it's the final architecture version. Every new capability from now on ships as a single `.py` file:

1. Download a plugin file (e.g. `calorie_counter.py`)
2. Drop it into the `plugins/` folder
3. Restart JARVIS — done. The skill is live, by voice, in any language.

Each plugin declares its own Gemini tool schema and logic in one file. The engine auto-discovers it at startup, registers it with the Live session, and lists it in the new **🧩 Plugin Manager** panel where every plugin gets its own persistent ON/OFF toggle.

Safety is built in at three layers: a broken or badly written plugin can **never** crash JARVIS — it simply shows up as "BROKEN" in the manager with the error explained, while every other tool and plugin keeps working. Name collisions with core tools are detected and rejected automatically. Want to write your own? Copy `plugins/_template.py` and fill in two things: the `PLUGIN` dict and the `run()` function.

### 📦 Plugin Guide

Plugins are optional drop-in extensions. The core project works without installing any extra plugin. To use one:

1. Get a plugin from a trusted source.
2. Place its `.py` file directly inside the project's `plugins/` directory.
3. Restart JARVIS so the plugin loader can discover and validate it.
4. Open the Plugin Manager and enable the plugin before using its voice command.

Every plugin should contain a `PLUGIN` metadata dictionary and a `run()` function. Use `plugins/_template.py` as the starting point. Keep plugin code self-contained, give each tool a unique name, validate user input, and clearly document required packages or credentials. A plugin may interact with external services, read local files, or control devices, so review its source before enabling it and never share API keys inside a plugin file.

If a plugin fails validation or raises an error, the loader isolates it and marks it as **BROKEN** rather than stopping the rest of JARVIS. Disable and remove untrusted or malfunctioning plugins, then restart the application after making changes. Plugin requests, troubleshooting, and community-distributed plugins are available on Discord: [Join the JARVIS plugin community](https://discord.gg/6ANGxWGaBk).

### 💓 Affective Dialog — JARVIS Hears How You Feel
Powered by Gemini Live's native audio understanding, JARVIS now picks up the emotion in your voice — excitement, frustration, fatigue — and adapts its own tone in response. Late-night tired questions get calm answers; excited announcements get energy back.

### 🤫 Proactive Audio — Knows When You're Not Talking to It
The biggest quality-of-life upgrade for an always-listening assistant: JARVIS can now tell when speech isn't addressed to it. Talking to someone in the room, taking a phone call, TV in the background — it stays silent instead of interjecting. No wake word needed, no accidental replies.

### ♾️ Unlimited Session Length — The Conversation Never Dies
Sliding-window context compression means the Live session no longer terminates when the context window fills up. Combined with session resumption, JARVIS holds one continuous conversation for hours without losing the thread.

All three Live API upgrades degrade gracefully: if the preview API ever rejects them, JARVIS automatically reconnects with the standard configuration — users never see a crash.

---

## 🗺️ Mark Roadmap

| Mark | Focus |
|---|---|
| **XLVIII** | Instant interrupt · parallel news · two-phase briefing · exponential backoff · vision cooldown |
| **XLIX** | Auto-start · clipboard intelligence · assistant customization |
| **L** | Session memory · background monitoring · proactive 2.0 · instant vision · parallel news search |
| **LI** | Plugin system · affective dialog · proactive audio · unlimited sessions |
| **LII+** | Plugin files: email · quiz mode · calorie counter · calendar · and more |

---

## ⚡ Quick Start

```bash
git clone https://github.com/msxfury/JARVIS-Mark-LI.git
cd JARVIS-Mark-LI
pip install -r requirements.txt
python main.py
```

> ⚠️ **Installation Note:** Some OS-specific dependencies are not bundled in `requirements.txt` to keep the repo lightweight. If you hit a `ModuleNotFoundError`, install the missing package with `pip install <module_name>`.

---

## 📋 Requirements

| Requirement | Details |
| --- | --- |
| **OS** | Windows 10/11, macOS, or Linux |
| **Python** | 3.11 or 3.12 |
| **Microphone** | Required for voice interaction |
| **API Key** | Free Gemini API key (`config/api_keys.json`) |

---

## 🗂️ Project Structure

```
Mark LI/
├── main.py                   # Core loop — Gemini Live session, audio I/O, tool dispatch
├── ui.py                     # PyQt6 HUD — waveform, log panel, plugin manager, camera feed
├── setup.py                  # First-run configuration wizard
├── plugins/
│   └── _template.py          # Copy this to write a new plugin — one file, drop in, done
├── actions/
│   ├── web_search.py         # Gemini + DDG parallel search (news, research, price, compare)
│   ├── screen_processor.py   # Screen capture & webcam vision via Gemini Live
│   ├── background_monitor.py # User-configured topic watching — daily DDG check, no crypto
│   ├── proactive.py          # Proactive 2.0 — time/context/rotation-aware check-ins
│   ├── reminder.py           # OS-native scheduled notifications
│   ├── system_monitor.py     # CPU / RAM / GPU / temperature telemetry
│   ├── computer_settings.py  # Volume, brightness, WiFi, power
│   ├── computer_control.py   # Keyboard shortcuts, mouse, window management
│   ├── open_app.py           # Application launcher
│   ├── browser_control.py    # Web browser control
│   ├── file_controller.py    # File system operations
│   ├── file_processor.py     # Document reading and summarization
│   ├── send_message.py       # Messaging integration
│   ├── weather_report.py     # Live weather data
│   ├── flight_finder.py      # Flight search
│   ├── youtube_video.py      # YouTube playback control
│   ├── game_updater.py       # Game update management (Steam / Epic)
│   ├── code_helper.py        # Code review and generation
│   ├── dev_agent.py          # Developer task agent
│   └── desktop.py            # Desktop and taskbar control
├── memory/
│   ├── memory_manager.py     # Load/save long_term.json — sessions, monitors, identity
│   └── long_term.json        # Persistent store: identity, preferences, projects, sessions, monitors
├── core/
│   ├── prompt.txt            # Assistant personality and tool-routing rules
│   └── plugin_loader.py      # Plugin engine — discovery, validation, crash isolation
└── config/
    └── api_keys.json         # API key, OS setting, assistant name, user name
```

---

## ⚠️ License

Personal and non-commercial use only.
Licensed under **[Creative Commons BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/)**.

---

## 🤝 Contributors and Community

This project is maintained and published by **msxfury**. Contributions are welcome when they improve reliability, privacy, accessibility, cross-platform support, or useful assistant capabilities.

### Contributing Code

1. Fork the repository and create a focused feature or fix branch.
2. Follow the existing Python style and keep changes scoped to the problem.
3. For new plugins, start from `plugins/_template.py`, include clear metadata, avoid hard-coded secrets, and document setup requirements.
4. Test the assistant and the affected plugin on your supported operating system.
5. Open a pull request describing the behavior changed, dependencies added, permissions required, and any setup steps.

Please do not submit API keys, private certificates, personal data, generated `.pyc` files, or unrelated refactors. By contributing, you agree that your work may be included in this project under its existing license.

⭐ **Star the repository to support the journey to Mark 100.**

| Platform | Link |
| --- | --- |
| YouTube | [@FatihMakes](https://www.youtube.com/@FatihMakes) |
| Instagram | [@fatihmakes](https://www.instagram.com/fatihmakes) |
| Discord | [JARVIS Plugin Community](https://discord.gg/6ANGxWGaBk) |
