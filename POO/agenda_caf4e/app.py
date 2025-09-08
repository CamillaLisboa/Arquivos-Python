from flask import Flask, render_template, request, redirect, url_for, flash
from services.agenda_service import AgendaService
from infrastructure.sqlite_repository import SQLiteAgendaRepository
import os

def create_app(db_path=None):
    app = Flask(__name__)
    app.secret_key = "dev-secret-key"  # para flash messages

    if db_path is None:
        db_path = os.path.join(os.path.dirname(__file__), "data", "agenda.db")
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    repo = SQLiteAgendaRepository(db_path=db_path)
    service = AgendaService(repo)

    @app.route("/")
    def home():
        events = service.list_events()
        students = service.list_students()
        return render_template("index.html", events=events, students=students)

    # ---------- Eventos ----------
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

    @app.get("/events/<int:event_id>/edit")
    def edit_event(event_id: int):
        event = service.get_event(event_id)
        if not event:
            flash("Evento não encontrado.")
            return redirect(url_for("home"))
        return render_template("event_edit.html", event=event)

    @app.post("/events/<int:event_id>/edit")
    def update_event(event_id: int):
        title = request.form.get("title") or "Café da manhã"
        date = request.form.get("date")
        if not date:
            flash("Informe a data.")
            return redirect(url_for("edit_event", event_id=event_id))
        service.update_event(event_id, title, date)
        flash("Evento atualizado!")
        return redirect(url_for("home"))

    @app.post("/delete-event")
    def delete_event():
        eid = request.form.get("event_id")
        if eid:
            service.delete_event(int(eid))
            flash("Evento excluído.")
        return redirect(url_for("home"))

    # ---------- Participações ----------
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

    @app.get("/participations/<int:pid>/edit")
    def edit_participation(pid: int):
        part = service.get_participation(pid)
        if not part:
            flash("Participação não encontrada.")
            return redirect(url_for("home"))
        # também trazemos o aluno para editar nome/contato
        student = service.get_student(part.student_id)
        return render_template("participation_edit.html", part=part, student=student)

    @app.post("/participations/<int:pid>/edit")
    def update_participation(pid: int):
        item = request.form.get("item")
        student_name = request.form.get("student_name")
        student_contact = request.form.get("student_contact")
        event_id = request.form.get("event_id")  # para voltar suave

        if not item or not student_name:
            flash("Informe pelo menos o item e o nome do aluno.")
            return redirect(url_for("edit_participation", pid=pid))

        part = service.get_participation(pid)
        if not part:
            flash("Participação não encontrada.")
            return redirect(url_for("home"))

        # Atualiza aluno (nome/contato) e participação (item)
        service.update_student(part.student_id, student_name, student_contact or "")
        service.update_participation(pid, item)
        flash("Participação atualizada!")
        return redirect(url_for("home"))

    @app.post("/delete-participation")
    def delete_participation():
        pid = request.form.get("participation_id")
        if pid:
            service.remove_participation(int(pid))
            flash("Participação removida.")
        return redirect(url_for("home"))

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
