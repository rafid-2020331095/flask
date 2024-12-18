import time
from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route("/")
@app.route("/jungle")
@app.route("/mungle")
def home():
    return "<h1>hello rafid adib.welcome</h1>"

@app.route("/pass/<sname>/<int:smarks>")
def passed(sname,smarks):
    return f"<h1>{sname} u have passed with {smarks} marks</h1>"

@app.route("/fail/<sname>/<int:smarks>")
def failed(sname,smarks):
    return f"<h1>{sname} u have failed with {smarks} marks</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        time.sleep(1)
        return redirect(url_for("failed",sname=name,smarks=num))

    else:
        time.sleep(1)
        return redirect(url_for("passed",sname=name,smarks=num))

if __name__=="__main__":
    app.run(debug=True)
