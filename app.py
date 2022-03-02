from crypt import methods
from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/sub", methods=['POST'])
def submit():
    # HTML to Python file
    if request.method == "POST":
        name = request.form["username"]
    
    #.py to HTML
    return render_template("submit.html",n=name)

if __name__== "__main__": 
  app.run(debug=True)
  