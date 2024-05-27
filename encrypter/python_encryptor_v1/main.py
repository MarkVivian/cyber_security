from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
  error = None
  if request.method == "POST":
    username = request.form["username"]
    password = request.form["password"]
    # Simulate login logic (replace with your actual authentication)
    if username == "admin" and password == "password":
      return render_template("success.html")
    else:
      error = "Invalid username or password!"
  return render_template("login.html", error=error)

@app.route("/success.html")
def success():
  return render_template("success.html")

if __name__ == "__main__":
  app.run(debug=True)
