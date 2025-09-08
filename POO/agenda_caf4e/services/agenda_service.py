from domain.interfaces import Repository, Notifier
from domain.person import Student

class AgendaService:
    def __init__(self, repository: Repository, notifier: Notifier | None = None):
        self._repo = repository
        self._notifier = notifier

    @property
    def notifier(self) -> Notifier | None:
        return self._notifier

    @notifier.setter
    def notifier(self, n: Notifier | None):
        self._notifier = n

    def create_event(self, title: str, date: str):
        event_id = self._repo.create_event(title=title, date=date)
        if self._notifier:
            self._notifier.notify(f"Novo evento criado: {title} em {date} (id={event_id})")
        return event_id

    def list_events(self):
        return self._repo.list_events()

    def delete_event(self, event_id: int):
        self._repo.delete_event(event_id)

    def get_event(self, event_id: int):
        return self._repo.get_event(event_id)

    def ensure_student(self, name: str, contact: str = "") -> Student:
        return self._repo.ensure_student(name=name, contact=contact)

    def list_students(self):
        return self._repo.list_students()

    def add_participation(self, event_id: int, student_id: int, item: str):
        pid = self._repo.add_participation(event_id, student_id, item)
        if self._notifier:
            self._notifier.notify(f"Participação adicionada (event={event_id} student={student_id} item='{item}')")
        return pid

    def remove_participation(self, participation_id: int):
        self._repo.remove_participation(participation_id)
