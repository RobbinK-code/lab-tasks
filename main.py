"""Simple CLI for the Task Management System.

Provides: add task, mark complete, view pending, and show progress.

Tasks are persisted to `tasks.json` in the same directory.
"""
import sys

import task_utils as utils
from validation import is_valid_index


def print_menu() -> None:
    print()
    print("Task Manager")
    print("1) Add task")
    print("2) Mark task complete")
    print("3) View pending tasks")
    print("4) Show progress")
    print("5) Quit")


def main() -> None:
    tasks = utils.load_tasks()
    while True:
        print_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            title = input("Task title: ").strip()
            description = input("Description (optional): ").strip()
            try:
                utils.add_task(tasks, title, description)
                utils.save_tasks(tasks)
                print("Task added.")
            except ValueError as e:
                print("Error:", e)
        elif choice == "2":
            if not tasks:
                print("No tasks available.")
                continue
            for i, t in enumerate(tasks):
                status = "✓" if t.get("completed") else " "
                print(f"[{i}] {status} {t['title']}")
            index = input("Index to mark complete: ").strip()
            if not is_valid_index(index, tasks):
                print("Invalid index.")
                continue
            utils.mark_complete(tasks, index)
            utils.save_tasks(tasks)
            print("Task marked complete.")
        elif choice == "3":
            pending = utils.list_pending(tasks)
            if not pending:
                print("No pending tasks.")
            else:
                for i, t in pending:
                    desc = t.get("description")
                    if desc:
                        print(f"[{i}] {t['title']} - {desc}")
                    else:
                        print(f"[{i}] {t['title']}")
        elif choice == "4":
            print(f"Progress: {utils.progress(tasks)}%")
        elif choice == "5" or choice.lower() == "q":
            utils.save_tasks(tasks)
            print("Goodbye.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
        sys.exit(0)
