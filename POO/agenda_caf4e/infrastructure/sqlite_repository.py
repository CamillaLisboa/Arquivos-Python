import os
import sqlite3
from typing import List, Optional
from domain.interfaces import Repository
from domain.event import BreakfastEvent, Participation
from domain.person import Student

class SQLiteAgendaRepository(Repository):
    """
    Implementa a interface Repository usando sqlite3 nativo.
    """
    def __init__(self, db_path: str):
        self.db_path = os.path.abspath(db_path)
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        self.init_db()

    def connect(self):
        conn = sqlite3.connect(self.db_path, timeout=10)
        conn.row_factory = sqlite3.Row
        return conn

    def init_db(self) -> None:
        with self.connect() as conn:
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    contact TEXT DEFAULT ''
                )
            """)
            c.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    date TEXT NOT NULL
                )
            """)
            c.execute("""
                CREATE TABLE IF NOT EXISTS participations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_id INTEGER NOT NULL,
                    student_id INTEGER NOT NULL,
                    item TEXT NOT NULL,
                    FOREIGN KEY(event_id) REFERENCES events(id) ON DELETE CASCADE,
                    FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
                )
            """)
            conn.commit()

    # --- Events ---
    def create_event(self, title: str, date: str) -> int:
        with self.connect() as conn:
            cur = conn.execute("INSERT INTO events (title, date) VALUES (?, ?)", (title, date))
            conn.commit()
            return cur.lastrowid

    def update_event(self, event_id: int, title: str, date: str) -> None:
        with self.connect() as conn:
            conn.execute("UPDATE events SET title = ?, date = ? WHERE id = ?", (title, date, event_id))
            conn.commit()

    def delete_event(self, event_id: int) -> None:
        with self.connect() as conn:
            conn.execute("DELETE FROM participations WHERE event_id = ?", (event_id,))
            conn.execute("DELETE FROM events WHERE id = ?", (event_id,))
            conn.commit()

    def list_events(self) -> List[BreakfastEvent]:
        with self.connect() as conn:
            rows = conn.execute("SELECT id, title, date FROM events ORDER BY date ASC, id DESC").fetchall()
            events = []
            for r in rows:
                event = BreakfastEvent(event_id=r["id"], title=r["title"], date_str=r["date"])
                parts = conn.execute("""
                    SELECT p.id, p.event_id, p.student_id, p.item, s.name AS student_name
                    FROM participations p
                    JOIN students s ON s.id = p.student_id
                    WHERE p.event_id = ?
                    ORDER BY p.id DESC
                """, (event.id,)).fetchall()
                for pr in parts:
                    event.add_participation(Participation(pr["id"], pr["event_id"], pr["student_id"], pr["student_name"], pr["item"]))
                events.append(event)
            return events

    def get_event(self, event_id: int) -> Optional[BreakfastEvent]:
        with self.connect() as conn:
            r = conn.execute("SELECT id, title, date FROM events WHERE id = ?", (event_id,)).fetchone()
            if not r:
                return None
            event = BreakfastEvent(event_id=r["id"], title=r["title"], date_str=r["date"])
            parts = conn.execute("""
                SELECT p.id, p.event_id, p.student_id, p.item, s.name AS student_name
                FROM participations p
                JOIN students s ON s.id = p.student_id
                WHERE p.event_id = ?
                ORDER BY p.id DESC
            """, (event_id,)).fetchall()
            for pr in parts:
                event.add_participation(Participation(pr["id"], pr["event_id"], pr["student_id"], pr["student_name"], pr["item"]))
            return event

    # --- Students ---
    def ensure_student(self, name: str, contact: str) -> Student:
        with self.connect() as conn:
            r = conn.execute("SELECT id, name, contact FROM students WHERE LOWER(name) = LOWER(?)", (name.strip(),)).fetchone()
            if r:
                return Student(r["name"], r["contact"], sid=r["id"])
            cur = conn.execute("INSERT INTO students (name, contact) VALUES (?, ?)", (name.strip(), contact.strip()))
            conn.commit()
            return Student(name.strip(), contact.strip(), sid=cur.lastrowid)

    def get_student(self, student_id: int) -> Optional[Student]:
        with self.connect() as conn:
            r = conn.execute("SELECT id, name, contact FROM students WHERE id = ?", (student_id,)).fetchone()
            if not r:
                return None
            return Student(r["name"], r["contact"], sid=r["id"])

    def update_student(self, student_id: int, name: str, contact: str) -> None:
        with self.connect() as conn:
            conn.execute("UPDATE students SET name = ?, contact = ? WHERE id = ?", (name.strip(), contact.strip(), student_id))
            conn.commit()

    def list_students(self) -> List[Student]:
        with self.connect() as conn:
            rows = conn.execute("SELECT id, name, contact FROM students ORDER BY name ASC").fetchall()
            return [Student(r["name"], r["contact"], sid=r["id"]) for r in rows]

    # --- Participation ---
    def add_participation(self, event_id: int, student_id: int, item: str) -> int:
        with self.connect() as conn:
            cur = conn.execute(
                "INSERT INTO participations (event_id, student_id, item) VALUES (?, ?, ?)",
                (event_id, student_id, item.strip())
            )
            conn.commit()
            return cur.lastrowid

    def get_participation(self, participation_id: int) -> Optional[Participation]:
        with self.connect() as conn:
            r = conn.execute("""
                SELECT p.id, p.event_id, p.student_id, p.item, s.name AS student_name
                FROM participations p
                JOIN students s ON s.id = p.student_id
                WHERE p.id = ?
            """, (participation_id,)).fetchone()
            if not r:
                return None
            return Participation(r["id"], r["event_id"], r["student_id"], r["student_name"], r["item"])

    def update_participation(self, participation_id: int, item: str) -> None:
        with self.connect() as conn:
            conn.execute("UPDATE participations SET item = ? WHERE id = ?", (item.strip(), participation_id))
            conn.commit()

    def remove_participation(self, participation_id: int) -> None:
        with self.connect() as conn:
            conn.execute("DELETE FROM participations WHERE id = ?", (participation_id,))
            conn.commit()
