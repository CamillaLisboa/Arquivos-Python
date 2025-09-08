import sqlite3
from pathlib import Path

APP_DIR = Path(__file__).parents[1]
DB_PATH = APP_DIR / "data" / "app.db"

def get_db():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con

def init_db():
    APP_DIR.joinpath("data").mkdir(exist_ok=True, parents=True)
    con = get_db()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS calculos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            genero TEXT NOT NULL,
            idade INTEGER NOT NULL,
            salario REAL NOT NULL,
            contribuicao INTEGER NOT NULL,
            taxa REAL NOT NULL,
            beneficio REAL NOT NULL,
            minimo_idade INTEGER NOT NULL,
            faltam_anos INTEGER NOT NULL,
            ano_estimado INTEGER NOT NULL,
            criado_em TEXT DEFAULT CURRENT_TIMESTAMP
        );
    """)
    con.commit()
    con.close()

def save_result(res: dict):
    con = get_db()
    cur = con.cursor()
    cur.execute("""
        INSERT INTO calculos
        (nome, genero, idade, salario, contribuicao, taxa, beneficio, minimo_idade, faltam_anos, ano_estimado)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (
        res["name"], res["gender"], res["age"], res["salary"], res["contrib_years"],
        res["replacement_rate"], res["estimated_benefit"], res["min_age"],
        res["years_left"], res["estimated_year"]
    ))
    con.commit()
    con.close()

def last_calculations(limit: int = 25):
    con = get_db()
    cur = con.cursor()
    cur.execute("""
        SELECT id, nome, genero, idade, salario, contribuicao, taxa, beneficio,
               minimo_idade, faltam_anos, ano_estimado, criado_em
        FROM calculos ORDER BY id DESC LIMIT ?;
    """, (limit,))
    rows = cur.fetchall()
    con.close()
    return rows
