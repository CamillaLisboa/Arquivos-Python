from flask import Flask, render_template, request, redirect, url_for, flash
from services.agenda_service import AgendaService
from infrastructure.sqlite_repository import SQLiteAgendaRepository
import os

def create_app(db_path=None):
    app = Flask(__name__)
    app.secret_key = "dev-secret-key"

    if db_path is None:
        db_path = os.path.join(os.path.dirname(__file__), "data", "agenda.db")

    repo = SQLiteAgendaRepository(db_path=db_path)
    service = AgendaService(repo)

    @app.route("/")
    def home():
        events = service.list_events()
        students = service.list_students()
        return render_template("index.html", events=events, students=students)

    @app.post("/add-event")
    def add_event():
        date = request.form.get("date")
        title = request.form.get("title") or "Café da manhã"
        if not date:
            flash("Por favor, informe a data do evento.")
            return redirect(url_for("home"))
        service.create_event(title=title, date=date)
        flash("Evento criado com sucesso!")
        return redirect(url_for("home"))

    @app.post("/add-participant")
    def add_participant():
        event_id = request.form.get("event_id")
        name = request.form.get("name")
        item = request.form.get("item")
        contact = request.form.get("contact")  # opcional

        if not (event_id and name and item):
            flash("Preencha todos os campos para adicionar um participante.")
            return redirect(url_for("home"))

        student = service.ensure_student(name=name, contact=contact or "")
        service.add_participation(event_id=int(event_id), student_id=student.id, item=item)
        flash("Participante adicionado com sucesso!")
        return redirect(url_for("home"))

    @app.post("/delete-participation")
    def delete_participation():
        pid = request.form.get("participation_id")
        if pid:
            service.remove_participation(int(pid))
            flash("Participação removida.")
        return redirect(url_for("home"))

    @app.post("/delete-event")
    def delete_event():
        eid = request.form.get("event_id")
        if eid:
            service.delete_event(int(eid))
            flash("Evento excluído.")
        return redirect(url_for("home"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
