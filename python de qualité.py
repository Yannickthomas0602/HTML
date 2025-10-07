#!/usr/bin/env python3
"""
Mini Todo CLI
Usage:
  python todo.py add "Titre de la tâche"
  python todo.py list
  python todo.py rm 2
"""
import sys
import json
from pathlib import Path

DATA_FILE = Path("todo_data.json")

def load_todos():
    if not DATA_FILE.exists():
        return []
    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except Exception:
        return []

def save_todos(todos):
    DATA_FILE.write_text(json.dumps(todos, ensure_ascii=False, indent=2), encoding="utf-8")

def cmd_add(args):
    if not args:
        print("Erreur: aucun titre fourni. Usage: python todo.py add \"Titre\"")
        return
    title = " ".join(args).strip()
    todos = load_todos()
    todos.append({"title": title})
    save_todos(todos)
    print(f"✓ Tâche ajoutée : {title}")

def cmd_list(_args):
    todos = load_todos()
    if not todos:
        print("Aucune tâche pour le moment. Utilise : python todo.py add \"Ma tâche\"")
        return
    for i, t in enumerate(todos, start=1):
        print(f"{i}. {t['title']}")

def cmd_rm(args):
    if not args or not args[0].isdigit():
        print("Usage: python todo.py rm <numéro>")
        return
    idx = int(args[0]) - 1
    todos = load_todos()
    if idx < 0 or idx >= len(todos):
        print("Indice invalide.")
        return
    removed = todos.pop(idx)
    save_todos(todos)
    print(f"✓ Tâche supprimée : {removed['title']}")

def help_msg():
    print(__doc__)

def main():
    if len(sys.argv) < 2:
        help_msg()
        return
    cmd = sys.argv[1]
    args = sys.argv[2:]
    if cmd == "add":
        cmd_add(args)
    elif cmd == "list":
        cmd_list(args)
    elif cmd == "rm":
        cmd_rm(args)
    else:
        help_msg()

if __name__ == "__main__":
    main()
"miam"