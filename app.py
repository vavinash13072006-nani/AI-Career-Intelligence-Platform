from flask import Flask, render_template, request
from waitress import serve

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():

    prediction = ""
    description = ""
    courses = []
    score = 0

    if request.method == "POST":

        skills = {

            "python": int(request.form.get("python", 0)),
            "java": int(request.form.get("java", 0)),
            "cpp": int(request.form.get("cpp", 0)),
            "javascript": int(request.form.get("javascript", 0)),
            "html": int(request.form.get("html", 0)),
            "react": int(request.form.get("react", 0)),
            "node": int(request.form.get("node", 0)),
            "sql": int(request.form.get("sql", 0)),
            "mongodb": int(request.form.get("mongodb", 0)),
            "ml": int(request.form.get("ml", 0)),
            "dl": int(request.form.get("dl", 0)),
            "analytics": int(request.form.get("analytics", 0)),
            "communication": int(request.form.get("communication", 0)),
            "problem": int(request.form.get("problem", 0)),
            "git": int(request.form.get("git", 0))
        }

        score = sum(skills.values())

        # AI / ML Engineer
        if (
            skills["python"] and
            skills["ml"] and
            skills["dl"]
        ):

            prediction = "AI / Machine Learning Engineer"

            description = "Strong profile for AI, NLP, Deep Learning and Computer Vision roles."

            courses = [
                "Deep Learning",
                "NLP",
                "Computer Vision",
                "MLOps"
            ]

        # Full Stack Developer
        elif (
            skills["javascript"] and
            skills["react"] and
            skills["node"]
        ):

            prediction = "Full Stack Developer"

            description = "Suitable for modern web application development and scalable backend systems."

            courses = [
                "React Advanced",
                "Node.js",
                "MongoDB",
                "REST APIs"
            ]

        # Data Scientist
        elif (
            skills["python"] and
            skills["analytics"] and
            skills["sql"]
        ):

            prediction = "Data Scientist"

            description = "Suitable for data analytics, AI models and business intelligence."

            courses = [
                "Data Science",
                "Statistics",
                "Power BI",
                "Data Visualization"
            ]

        # Backend Developer
        elif (
            skills["java"] and
            skills["sql"]
        ):

            prediction = "Backend Developer"

            description = "Strong backend and database-oriented development profile."

            courses = [
                "Spring Boot",
                "SQL Optimization",
                "System Design",
                "APIs"
            ]

        # Software Engineer
        elif (
            skills["cpp"] and
            skills["problem"]
        ):

            prediction = "Software Engineer"

            description = "Strong logical and problem-solving oriented engineering profile."

            courses = [
                "DSA",
                "Competitive Programming",
                "Operating Systems",
                "System Design"
            ]

        else:

            prediction = "Beginner Developer"

            description = "Develop more technical skills to unlock advanced career opportunities."

            courses = [
                "Programming Fundamentals",
                "Python",
                "GitHub",
                "Web Development"
            ]

    return render_template(
        "index.html",
        prediction=prediction,
        description=description,
        courses=courses,
        score=score
    )

if __name__ == "__main__":

    print("Server running at: http://127.0.0.1:5000")

    serve(app, host="127.0.0.1", port=5000)