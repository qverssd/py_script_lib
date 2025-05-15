notes = []
next_id = 1

def add_note(text):
    global next_id
    note = {"id": next_id, "text": text}
    notes.append(note)
    next_id +=1
    return note

def delete_note_by_id(note_id):
    global notes
    for note in notes:
        if note["id"] == note_id:
            notes = [n for n in notes if n["id"] !=note_id]
            return True
    return False