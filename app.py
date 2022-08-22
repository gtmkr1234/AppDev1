from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/hello", methods = ["GET","POST"])
def hello_world():
    if(request.method=="GET"):
        return render_template("form.html")

    elif (request.method=="POST"):
        username = request.form["user_name"]
        return render_template("friend.html",display_name=username )




if __name__ == '__main__':
    app.debug=True
    app.run()