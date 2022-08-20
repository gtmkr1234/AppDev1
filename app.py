from flask import Flask
from flask import render_template
app = Flask(__name__)
@app.route("/hello", methods = ["GET","POST"])
def hello_world():
    return render_template("form.html")

if __name__ == '__main__':
    app.debug=True
    app.run()


