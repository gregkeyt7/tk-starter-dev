from flask import Flask, render_template, request, redirect, url_for
import sqlite3, os

app = Flask(__name__)
DB_PATH = os.path.join(os.path.dirname(__file__), "todo.db")

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS todos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            done INTEGER NOT NULL DEFAULT 0
        )""")
init_db()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        if title:
            with sqlite3.connect(DB_PATH) as conn:
                conn.execute("INSERT INTO todos (title, done) VALUES (?, 0)", (title,))
        return redirect(url_for("index"))

    with sqlite3.connect(DB_PATH) as conn:
        todos = conn.execute("SELECT id, title, done FROM todos ORDER BY id DESC").fetchall()
    return render_template("index.html", todos=todos)

@app.post("/toggle/<int:todo_id>")
def toggle(todo_id):
    with sqlite3.connect(DB_PATH) as conn:
        row = conn.execute("SELECT done FROM todos WHERE id=?", (todo_id,)).fetchone()
        if row:
            new_val = 0 if row[0] else 1
            conn.execute("UPDATE todos SET done=? WHERE id=?", (new_val, todo_id))
    return redirect(url_for("index"))

@app.post("/delete/<int:todo_id>")
def delete(todo_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("DELETE FROM todos WHERE id=?", (todo_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
