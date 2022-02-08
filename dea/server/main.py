from flask import Flask, make_response,request,redirect
import hashlib
import random
import requests as req
import sys
sys.path.append("/home/arancha/progr_master/dea")
from auth import Auth

SECRET = "4cfa98d37472801305b5d4a85bc98e6a9b4b0213de8762c35336a2b1a586c055"

app = Flask(__name__)
auth = Auth(SECRET,request)


@app.route("/dea/login")
def log_in():
    email = "a@test.com"
    pwd = "1234"
    if auth.validate_pwd(pwd):
        res = make_response("Log in")
        token = auth.gen_token()
        res.set_cookie("token",token)
        req.post("http://localhost:3000/dea/api", data={"email":email,"token":token})
        return res
    return "wrong pwd"

@app.route("/dea/secret")
@auth.token
def secret():
    return "Secret"

if __name__ == "__main__":
    app.run(debug=True,port=5000)