from venv import create
from flask import Flask, request, g, make_response,Response
from flask_cors import CORS
import sqlite3
from funcs import *

app = Flask(__name__)
CORS(app)

DB = "./deas.db"

def con():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
        db.row_factory = sqlite3.Row
    return db


@app.route("/dea/api")
def api():
    return Response(get_all(con,"users"), content_type="application/json")

@app.route("/dea/api/token", methods=["PUT", "GET"])
def token():
    cur = con().cursor()
    verb = request.method 
    if verb == "PUT":
        email = request.form.get("email")
        pwd = request.form.get("pwd")
        token = request.form.get("token")

        user = next(cur.execute(f'''SELECT * FROM users WHERE email='{email}';'''), {})
        if dict(user).get("pwd") == pwd:
            cur.execute(f'''UPDATE users SET token='{token}' WHERE email='{email}';''')
            con().commit()
            return {"success": True, "id": user["id"], "token": token}
        return {"success": False, "msg": "User not found!"}

    elif verb == "GET":
        cookie_id = request.args.get("id")
        cookie_token = request.args.get("token")

        print(f"COOKIE_ID: {cookie_id}")
        user = next(cur.execute(f'''SELECT * FROM users WHERE id='{cookie_id}';'''), {})
        if dict(user).get("token") == cookie_token:
            return {"success": True}

    return {"success": False}

@app.route("/dea/api/signup", methods=["GET","POST"])
def api_signup():
    cur = con().cursor()
    if request.method == "POST":
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        print(email, pwd)
        print(request.form)
        if email and pwd:
            query = f'''INSERT INTO users VALUES ('{create_id(cur)}','{email}','{pwd}','');'''
            print(query)
            cur.execute(f'''INSERT INTO users VALUES ('{create_id(cur)}','{email}','{pwd}','');''')
            con().commit()
            return {"success":True}
        return {"success":False}
    if request.method == "GET":
        return {"success":True}


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == "__main__":
    app.run(debug=True, port=3000)
