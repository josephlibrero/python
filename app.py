from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # A list to store tasks

@app.route("/")
def home():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    if task:
        tasks.append({"name": task, "completed": False})
    return redirect("/")

@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    tasks[task_id]["completed"] = True
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)