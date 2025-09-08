# Agenda de Cafés da Manhã (Flask + SQLite)

Projeto didático para organizar cafés da manhã entre alunos:
- Cadastre datas de eventos;
- Para cada evento, adicione alunos e o que cada um vai trazer;
- Visual clean, responsivo e simples.

## Como rodar

```bash
cd agenda_cafe
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
python app.py
# abra http://127.0.0.1:5000
```

## OOP / SOLID (resumo)
- domain/person.py — Person (classe base) e Student (herança). Encapsulamento com @property.
- domain/event.py — BreakfastEvent agrega Participation (composição/agregação).
- domain/interfaces.py — interfaces Repository e Notifier.
- infrastructure/sqlite_repository.py — implementação concreta SQLiteAgendaRepository (DIP).
- infrastructure/notifiers.py — implementações de Notifier (polimorfismo).
- services/agenda_service.py — regras de negócio / orquestração.
- app.py — Flask (camada de apresentação).
