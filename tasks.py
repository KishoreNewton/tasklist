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


def show():
    tasks = load()
    if not tasks:
        print("No tasks yet.")
    for number, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{number}. [{mark}] {task['title']}")
    print(sum(1 for t in tasks if not t["done"]), "open")


def done(number):
    tasks = load()
    tasks[number - 1]["done"] = True
    save(tasks)


if __name__ == "__main__":
    command = sys.argv[1]
    if command == "add":
        add(sys.argv[2])
    elif command == "list":
        show()
    elif command == "done":
        number = int(sys.argv[2])
        if 1 <= number <= len(load()):
            done(number)
        else:
            print(f"There is no task {number}.")
    elif command == "remove":
        tasks = load()
        del tasks[int(sys.argv[2]) - 1]
        save(tasks)
    elif command == "clear":
        save([t for t in load() if not t["done"]])
