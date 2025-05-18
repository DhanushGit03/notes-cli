import json
import os
import sys

NOTES_FILE = "notes.json"

def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    try:
        with open(NOTES_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)

def add_note(content):
    notes = load_notes()
    new_id = len(notes) + 1
    notes.append({"id": new_id, "content": content})
    save_notes(notes)
    print(f"✅ Note added with ID {new_id}.")

def list_notes():
    notes = load_notes()
    if not notes:
        print("📭 No notes found.")
        return
    for note in notes:
        print(f"[{note['id']}] {note['content']}")

def delete_note(note_id):
    notes = load_notes()
    updated_notes = [note for note in notes if note['id'] != note_id]

    if len(notes) == len(updated_notes):
        print(f"⚠️ No note found with ID {note_id}.")
        return

    # Reassign IDs to maintain order
    for i, note in enumerate(updated_notes, start=1):
        note['id'] = i

    save_notes(updated_notes)
    print(f"🗑️ Note with ID {note_id} deleted.")

def print_usage():
    print("\nUsage:")
    print("  python notes.py add \"Your note here\"")
    print("  python notes.py list")
    print("  python notes.py delete <note_id>\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("❗ Missing command.")
        print_usage()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "add" and len(sys.argv) >= 3:
        content = " ".join(sys.argv[2:])
        add_note(content)
    elif command == "list":
        list_notes()
    elif command == "delete" and len(sys.argv) == 3:
        try:
            note_id = int(sys.argv[2])
            delete_note(note_id)
        except ValueError:
            print("❗ Invalid note ID. It should be a number.")
    else:
        print("❗ Invalid command or arguments.")
        print_usage()
