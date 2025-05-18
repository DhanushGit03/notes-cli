import json
import os
import sys

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as file:
        return json.load(file)

def save_notes(notes):
    with open(NOTES_FILE, "w") as file:
        json.dump(notes, file, indent=2)

def add_note(content):
    notes = load_notes()
    notes.append({"id": len(notes)+1, "content": content})
    save_notes(notes)
    print("✅ Note added.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
    for note in notes:
        print(f"[{note['id']}] {note['content']}")

def delete_note(note_id):
    notes = load_notes()
    notes = [n for n in notes if n['id'] != note_id]
    for i, note in enumerate(notes):
        note['id'] = i + 1
    save_notes(notes)
    print("🗑️ Note deleted.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python notes.py [add/list/delete] [note]")
    else:
        command = sys.argv[1]
        if command == "add" and len(sys.argv) >= 3:
            content = " ".join(sys.argv[2:])
            add_note(content)
        elif command == "list":
            list_notes()
        elif command == "delete" and len(sys.argv) == 3:
            try:
                delete_note(int(sys.argv[2]))
            except ValueError:
                print("Invalid note ID.")
        else:
            print("Invalid command.")
