from flask import Flask,redirect,url_for
app=Flask(__name__)

@app.route("/")
@app.route("/jungle")
@app.route("/mungle")
def home():
    return "<h1>hello rafid adib.welcome</h1>"

@app.route("/pass")
def passed():
    return "<h1>u have passed</h1>"

@app.route("/fail")
def failed():
    return "<h1>u have failed</h1>"

@app.route("/score/<name>/<int:num>")
def score(name,num):
    if num<30:
        return redirect(url_for("failed"))

    else:
        
        return redirect(url_for("passed"))
    
    

if __name__=="__main__":
    app.run(debug=True)
