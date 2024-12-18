# from flask import Flask
# app=Flask(__name__)
# @app.route("/")
# @app.route("/jungle")
# @app.route("/mungle")
# def home():
#     return "<h1>hello rafid adib.welcome</h1>"
# @app.route("/welcome/<name>")
# def abta(name):
#     return f"<h1>welcome {name}!!! to this page</h1>"
# if __name__=="__main__":
#     app.run(debug=True)
from flask import Flask,redirect,url_for
help(redirect)