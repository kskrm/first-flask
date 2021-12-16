from flask import Flask,render_template,request,session,redirect

app = Flask(__name__)

registerd = []

@app.route("/")
def index():
    if request.method == "GET":
        # display form to request birthday
        return redirect("/register")

    if request.method == "POST":
        name = request.form.get("name")
        return render_template("index.html", name=name)

@app.route("/register")
def register():
    name = request.form["name"]
    team = ["Real Madrid","Manchester United","FC Barcelona","Manchester City"]
    all_onegai = OnegaiContent.query.all()
    return render_template("index.html", name=name, team=team, all_onegai=all_onegai)

if __name__ == "__main__":
    app.run(debug=True)