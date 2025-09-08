class Person:
    def __init__(self, name: str, contact: str = ""):
        self._name = name.strip()
        self._contact = contact.strip()

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        if not value or not value.strip():
            raise ValueError("Nome não pode ser vazio.")
        self._name = value.strip()

    @property
    def contact(self) -> str:
        return self._contact

    @contact.setter
    def contact(self, value: str):
        self._contact = (value or "").strip()


class Student(Person):
    def __init__(self, name: str, contact: str = "", sid: int | None = None):
        super().__init__(name, contact)
        self.id = sid
