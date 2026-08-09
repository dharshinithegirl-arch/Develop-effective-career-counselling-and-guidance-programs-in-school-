from flask import Flask, request, render_template_string

app = Flask(__name__)

# Career database
CAREERS = {
    "Computer Science": {
        "skills": ["python", "java", "programming", "problem solving"],
        "careers": [
            "Software Developer",
            "Data Analyst",
            "Web Developer"
        ]
    },
    "Commerce": {
        "skills": ["accounting", "finance", "business", "communication"],
        "careers": [
            "Accountant",
            "Financial Analyst",
            "Business Manager"
        ]
    },
    "Arts": {
        "skills": ["creativity", "communication", "writing", "design"],
        "careers": [
            "Content Writer",
            "Graphic Designer",
            "Teacher"
        ]
    }
}


# Career recommendation function
def recommend_career(stream, student_skills):

    if stream not in CAREERS:
        return None

    required_skills = CAREERS[stream]["skills"]

    matched_skills = set(student_skills) & set(required_skills)

    percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100

    return {
        "careers": CAREERS[stream]["careers"],
        "matched_skills": list(matched_skills),
        "percentage": round(percentage, 2)
    }


# HTML page
HTML = """
<!DOCTYPE html>
<html>
<head>

<title>Career Counselling System</title>

<style>

body {
    font-family: Arial, sans-serif;
    background: #f2f5f9;
    margin: 0;
    padding: 0;
}

.container {
    width: 500px;
    margin: 50px auto;
    background: white;
    padding: 30px;
    border-radius: 12px;
    box-shadow: 0 0 15px #ccc;
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin-top: 15px;
    font-weight: bold;
}

input, select {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
    box-sizing: border-box;
}

button {
    width: 100%;
    padding: 12px;
    margin-top: 20px;
    background: #2563eb;
    color: white;
    border: none;
    border-radius: 6px;
    cursor: pointer;
}

button:hover {
    background: #1d4ed8;
}

.result {
    margin-top: 25px;
    padding: 20px;
    background: #eef6ff;
    border-radius: 8px;
}

ul {
    line-height: 2;
}

</style>

</head>

<body>

<div class="container">

<h1>Career Counselling & Guidance</h1>

<form method="POST">

<label>Student Name</label>

<input type="text"
       name="name"
       placeholder="Enter your name"
       required>


<label>Select Your Stream</label>

<select name="stream" required>

<option value="">Select Stream</option>

<option value="Computer Science">
Computer Science
</option>

<option value="Commerce">
Commerce
</option>

<option value="Arts">
Arts
</option>

</select>


<label>Enter Your Skills</label>

<input type="text"
       name="skills"
       placeholder="python, programming, problem solving"
       required>


<button type="submit">
Get Career Recommendation
</button>

</form>


{% if result %}

<div class="result">

<h2>Career Recommendation</h2>

<p>
<b>Student:</b> {{ name }}
</p>

<p>
<b>Stream:</b> {{ stream }}
</p>

<p>
<b>Skill Match:</b>
{{ result.percentage }}%
</p>

<p>
<b>Matched Skills:</b>
{{ result.matched_skills }}
</p>


<h3>Recommended Careers</h3>

<ul>

{% for career in result.careers %}

<li>{{ career }}</li>

{% endfor %}

</ul>

</div>

{% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    result = None
    name = ""
    stream = ""

    if request.method == "POST":

        name = request.form["name"]

        stream = request.form["stream"]

        skills = request.form["skills"].lower().split(",")

        skills = [
            skill.strip()
            for skill in skills
        ]

        result = recommend_career(
            stream,
            skills
        )

    return render_template_string(
        HTML,
        result=result,
        name=name,
        stream=stream
    )


# Start application
if __name__ == "__main__":
    app.run(debug=True)
