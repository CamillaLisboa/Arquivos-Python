from typing import List, Optional

class Participation:
    def __init__(self, participation_id: int | None, event_id: int, student_id: int, student_name: str, item: str):
        self.id = participation_id
        self.event_id = event_id
        self.student_id = student_id
        self.student_name = student_name
        self.item = item

class BreakfastEvent:
    def __init__(self, event_id: int | None, title: str, date_str: str, participations: Optional[List[Participation]] = None):
        self.id = event_id
        self.title = title
        self.date = date_str
        self.participations = participations or []

    def add_participation(self, p: Participation):
        self.participations.append(p)

    def remove_participation(self, participation_id: int):
        self.participations = [p for p in self.participations if p.id != participation_id]
