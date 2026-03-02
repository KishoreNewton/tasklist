import json
import sys
from pathlib import Path

STORE = Path("tasks.json")


def load():
    if STORE.exists():
        return json.loads(STORE.read_text())
    return []


def save(tasks):
    STORE.write_text(json.dumps(tasks, indent=2))


def add(title):
    tasks = load()
    tasks.append({"title": title, "done": False})
    save(tasks)


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "add":
        add(sys.argv[2])
