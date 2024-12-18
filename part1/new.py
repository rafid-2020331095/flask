from flask import Flask
app=Flask(__name__)
@app.route("/")
@app.route("/jungle")
@app.route("/mungle")
def home():
    return "<h1>hello rafid adib.welcome</h1>"

@app.route("/about")
def abt():
    return "<h1>welcome to about page</h1>"


@app.route("/welcome/<name>")
def abta(name):
    return f"<h1>welcome {name}!!! to this page</h1>"

@app.route("/number/<int:name>")
def abtaa(name):
    return f"<h1>welcome {name+10}!!! to this page</h1>"
@app.route("/addition/<int:num1>/<int:num2>")
def abtaaa(num1,num2):
    return f"<h1>welcome {num1+num2}!!! to this page</h1>"
if __name__=="__main__":
    app.run(debug=True)
