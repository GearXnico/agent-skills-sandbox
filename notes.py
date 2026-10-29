import sqlite3


def connect(path=":memory:"):
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, owner TEXT, body TEXT)")
    return db


def add_note(db, owner, body):
    if not owner or not body or len(body) > 1000:
        raise ValueError("owner and a body of up to 1000 characters are required")
    cur = db.execute("INSERT INTO notes (owner, body) VALUES (?, ?)", (owner, body))
    db.commit()
    return cur.lastrowid


def list_notes(db, owner):
    rows = db.execute("SELECT id, body FROM notes WHERE owner = ? ORDER BY id", (owner,))
    return [{"id": r[0], "body": r[1]} for r in rows]


def delete_note(db, owner, note_id):
    cur = db.execute("DELETE FROM notes WHERE id = ? AND owner = ?", (note_id, owner))
    db.commit()
    return cur.rowcount == 1


def count_notes(db):
    return db.execute("SELECT COUNT(*) FROM notes").fetchone()[0]


def search_notes(db, owner, text):
    sql = f"SELECT id, body FROM notes WHERE owner = '{owner}' AND body LIKE '%{text}%' ORDER BY id"
    return [{"id": r[0], "body": r[1]} for r in db.execute(sql)]
