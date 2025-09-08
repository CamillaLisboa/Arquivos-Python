from flask import Flask, render_template, request, redirect, url_for, flash
from domain.models import Salary, Employee, RetirementCalculator, SimpleBrazilPolicy
from services.repository import init_db, save_result, last_calculations

app = Flask(__name__)
app.secret_key = "dev-secret"

# Inicializa DB
init_db()

# Policy (poderia ter outras — OCP)
policy = SimpleBrazilPolicy()
calculator = RetirementCalculator(policy)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular", methods=["GET", "POST"])
def calcular():
    if request.method == "POST":
        try:
            nome = request.form.get("nome","").strip()
            genero = (request.form.get("genero","") or "").lower()
            idade = int(request.form.get("idade","0"))
            salario = float(request.form.get("salario","0").replace(",", ".").strip())
            contribuicao = int(request.form.get("contribuicao","0"))

            emp = Employee(
                name=nome,
                age=idade,
                salary=Salary(salario),   # composição
                gender=genero,
                contrib_years=contribuicao
            )
            result = calculator.evaluate(emp)  # agregação com policy
            save_result(result)
            return render_template("resultado.html", r=result)

        except Exception as e:
            flash(f"Erro: {e}", "error")
            return redirect(url_for("calcular"))
    return render_template("calcular.html")

@app.route("/admin")
def admin():
    rows = last_calculations(50)
    return render_template("admin.html", rows=rows)

if __name__ == "__main__":
    app.run(debug=True)
