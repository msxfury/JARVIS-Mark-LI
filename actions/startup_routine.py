import json
import re
import sys
import time
import webbrowser
from datetime import datetime
from pathlib import Path

from actions.open_app import open_app


def _base_dir() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).parent
    return Path(__file__).resolve().parent.parent


ROUTINE_PATH = _base_dir() / "memory" / "startup_routine.json"
LONG_TERM_PATH = _base_dir() / "memory" / "long_term.json"


URL_ALIASES = {
    "chatgpt": "https://chatgpt.com/",
    "chat gpt": "https://chatgpt.com/",
    "openai chatgpt": "https://chatgpt.com/",
    "gmail": "https://mail.google.com/",
    "youtube": "https://www.youtube.com/",
    "instagram": "https://www.instagram.com/",
    "discord web": "https://discord.com/app",
}


APP_ALIASES = {
    "chrome": "Chrome",
    "google chrome": "Chrome",
    "discord": "Discord",
    "whatsapp": "WhatsApp",
    "instagram": "Instagram",
    "spotify": "Spotify",
    "vscode": "Visual Studio Code",
    "vs code": "Visual Studio Code",
    "visual studio code": "Visual Studio Code",
    "edge": "Edge",
    "firefox": "Firefox",
}


def _empty() -> dict:
    return {
        "enabled": False,
        "instruction": "",
        "steps": [],
        "updated": "",
        "last_run": "",
    }


def load_routine() -> dict:
    if ROUTINE_PATH.exists():
        try:
            data = json.loads(ROUTINE_PATH.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                base = _empty()
                base.update(data)
                return base
        except Exception:
            pass
    migrated = _migrate_long_term_routine()
    return migrated or _empty()


def save_routine(routine: dict) -> None:
    ROUTINE_PATH.parent.mkdir(parents=True, exist_ok=True)
    ROUTINE_PATH.write_text(json.dumps(routine, indent=2, ensure_ascii=False), encoding="utf-8")


def _memory_value(entry) -> str:
    if isinstance(entry, dict):
        return str(entry.get("value", "")).strip()
    return str(entry or "").strip()


def _migrate_long_term_routine() -> dict | None:
    if not LONG_TERM_PATH.exists():
        return None
    try:
        memory = json.loads(LONG_TERM_PATH.read_text(encoding="utf-8"))
        instruction = ""
        for section in ("preferences", "notes"):
            entry = memory.get(section, {}).get("startup_routine")
            instruction = _memory_value(entry)
            if instruction:
                break
        if not instruction:
            return None
        routine = _build_routine(instruction, enabled=True)
        save_routine(routine)
        return routine
    except Exception:
        return None


def _split_instruction(instruction: str) -> list[str]:
    text = re.sub(r"\b(set|make|save|mark)\b.*?\b(startup|start up)\b.*?\b(routine|phase 3)\b\s*(to|as)?", "", instruction, flags=re.I)
    text = re.sub(r"\bjarvis\b", "", text, flags=re.I)
    parts = re.split(r"\s*(?:,|\band\b|\bthen\b|\bafter that\b)\s*", text, flags=re.I)
    return [p.strip(" .") for p in parts if p.strip(" .")]


def _contains(text: str, *needles: str) -> bool:
    lower = text.lower()
    return any(n in lower for n in needles)


def _url_for(text: str) -> str:
    lower = text.lower()
    for key, url in URL_ALIASES.items():
        if key in lower:
            return url
    match = re.search(r"https?://\S+|(?:www\.)?[a-z0-9-]+\.[a-z]{2,}(?:/\S*)?", text, re.I)
    if match:
        url = match.group(0)
        if not url.startswith(("http://", "https://")):
            url = "https://" + url
        return url
    return ""


def _app_for(text: str) -> str:
    lower = text.lower()
    for key, app in APP_ALIASES.items():
        if key in lower:
            return app
    cleaned = re.sub(r"\b(open|launch|start|app|inside|in|the)\b", "", text, flags=re.I).strip(" .")
    return cleaned.title() if cleaned else ""


def parse_steps(instruction: str) -> list[dict]:
    steps: list[dict] = []
    chunks = _split_instruction(instruction)
    full_lower = instruction.lower()

    # Common phrase: "open Chrome inside ChatGPT" means open Chrome, then ChatGPT.
    if _contains(full_lower, "chrome") and _contains(full_lower, "chatgpt", "chat gpt"):
        steps.append({"type": "app", "target": "Chrome", "wait": 2.0})
        steps.append({"type": "url", "target": "https://chatgpt.com/", "wait": 2.5})

    for chunk in chunks:
        lower = chunk.lower()
        if _contains(lower, "chatgpt", "chat gpt") and any(s.get("target") == "https://chatgpt.com/" for s in steps):
            continue
        if _contains(lower, "chrome") and any(s.get("target") == "Chrome" for s in steps):
            continue
        if _contains(lower, "open", "launch", "start"):
            url = _url_for(chunk)
            if url and not any(s.get("target") == url for s in steps):
                if _contains(lower, "chrome", "browser"):
                    if not any(s.get("target") == "Chrome" for s in steps):
                        steps.append({"type": "app", "target": "Chrome", "wait": 2.0})
                steps.append({"type": "url", "target": url, "wait": 2.5})
                continue
            app = _app_for(chunk)
            if app and not any(s.get("type") == "app" and s.get("target").lower() == app.lower() for s in steps):
                steps.append({"type": "app", "target": app, "wait": 2.0})

    return steps


def _build_routine(instruction: str, enabled: bool = True) -> dict:
    return {
        "enabled": enabled,
        "instruction": instruction.strip(),
        "steps": parse_steps(instruction),
        "updated": datetime.now().isoformat(timespec="seconds"),
        "last_run": "",
    }


def _run_step(step: dict, player=None) -> str:
    kind = step.get("type")
    target = str(step.get("target", "")).strip()
    wait = float(step.get("wait", 1.0) or 1.0)
    if not target:
        return "Skipped empty startup step."
    if kind == "app":
        result = open_app(parameters={"app_name": target}, player=player)
    elif kind == "url":
        ok = webbrowser.open(target)
        result = f"Opened {target}." if ok else f"Could not open {target}."
    else:
        result = f"Unknown startup step type: {kind}"
    time.sleep(wait)
    return result


def run_startup_phase3(player=None, speak=None) -> str:
    routine = load_routine()
    if not routine.get("enabled"):
        return "Startup phase 3 is disabled."
    steps = routine.get("steps") or []
    if not steps:
        return "Startup phase 3 has no steps configured."

    results = []
    for step in steps:
        try:
            results.append(_run_step(step, player=player))
        except Exception as e:
            results.append(f"Startup step failed: {e}")

    routine["last_run"] = datetime.now().isoformat(timespec="seconds")
    save_routine(routine)
    return "Startup phase 3 complete: " + " ".join(results)


def startup_routine(parameters: dict, player=None, session_memory=None) -> str:
    params = parameters or {}
    action = (params.get("action") or "set").lower().strip()
    instruction = (params.get("instruction") or params.get("routine") or "").strip()

    if action in {"set", "save", "update"}:
        if not instruction:
            return "Please tell me what to do in the startup routine."
        routine = _build_routine(instruction, enabled=True)
        save_routine(routine)
        count = len(routine.get("steps", []))
        return f"Startup phase 3 routine saved with {count} step{'s' if count != 1 else ''}."

    if action in {"clear", "disable"}:
        routine = load_routine()
        routine["enabled"] = False
        save_routine(routine)
        return "Startup phase 3 routine disabled."

    if action == "enable":
        routine = load_routine()
        routine["enabled"] = True
        save_routine(routine)
        return "Startup phase 3 routine enabled."

    if action in {"show", "status"}:
        routine = load_routine()
        steps = routine.get("steps", [])
        if not routine.get("enabled"):
            return "Startup phase 3 is disabled."
        return f"Startup phase 3 is enabled with {len(steps)} step(s): {routine.get('instruction', '')}"

    if action == "run":
        return run_startup_phase3(player=player)

    return "Unknown startup routine action."
