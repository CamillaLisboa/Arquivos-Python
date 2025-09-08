from domain.interfaces import Notifier

class ConsoleNotifier(Notifier):
    def notify(self, message: str) -> None:
        print(f"[NOTIFY] {message}")

class DummyEmailNotifier(Notifier):
    def __init__(self, sender: str = "no-reply@escola.local"):
        self.sender = sender
    def notify(self, message: str) -> None:
        print(f"[EMAIL from {self.sender}] {message}")
