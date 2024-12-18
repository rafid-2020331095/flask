from flask import Flask,render_template,url_for
from employees import employees_data
app=Flask(__name__,)
@app.route("/")
@app.route("/jungle")
@app.route("/mungle")
def home():
    return render_template("home.html",title="home")

@app.route("/about")
def abt():
    return render_template("about.html",title="about")
@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html",title="evaluate",number=num)

@app.route("/employees")
def employees():
    return render_template("employees.html",title="employ_datas",employ=employees_data)

@app.route("/employees/managers")
def managers():
    return render_template("managers.html",title="managers_data",employ=employees_data)
if __name__=="__main__":
    app.run(debug=True)
