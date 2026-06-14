import json
import os
from typing import List, Dict, Tuple

from validation import is_non_empty_string, is_valid_index


TASKS_FILENAME = os.path.join(os.path.dirname(__file__), "tasks.json")


def _tasks_file(path: str = None) -> str:
    return path or TASKS_FILENAME


def load_tasks(path: str = None) -> List[Dict]:
    file = _tasks_file(path)
    if os.path.exists(file):
        try:
            with open(file, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


def save_tasks(tasks: List[Dict], path: str = None) -> None:
    file = _tasks_file(path)
    with open(file, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2, ensure_ascii=False)


def add_task(tasks: List[Dict], title: str, description: str = "") -> List[Dict]:
    if not is_non_empty_string(title):
        raise ValueError("Title must be a non-empty string")
    task = {"title": title.strip(), "description": (description or "").strip(), "completed": False}
    tasks.append(task)
    return tasks


def list_pending(tasks: List[Dict]) -> List[Tuple[int, Dict]]:
    return [(i, t) for i, t in enumerate(tasks) if not t.get("completed")]


def mark_complete(tasks: List[Dict], index) -> List[Dict]:
    if not is_valid_index(index, tasks):
        raise IndexError("Invalid task index")
    i = int(index)
    tasks[i]["completed"] = True
    return tasks


def progress(tasks: List[Dict]) -> int:
    if not tasks:
        return 0
    done = sum(1 for t in tasks if t.get("completed"))
    return int(done * 100 / len(tasks))
