from flask import Flask, render_template, request
from career_guidance import recommend_career

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/recommend", methods=["POST"])
def recommend():

    name = request.form["name"]
    stream = request.form["stream"]

    skills = request.form["skills"].lower().split(",")

    skills = [skill.strip() for skill in skills]

    result = recommend_career(stream, skills)

    return render_template(
        "result.html",
        name=name,
        stream=stream,
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)
