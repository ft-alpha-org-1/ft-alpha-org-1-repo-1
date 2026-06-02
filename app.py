"""Demo Flask app with a SQL injection vulnerability."""

import sqlite3

from flask import Flask, request

app = Flask(__name__)


@app.route("/user")
def get_user():
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE id = " + user_id
    cursor.execute(query)
    return {"rows": cursor.fetchall()}


if __name__ == "__main__":
    app.run(debug=True)
