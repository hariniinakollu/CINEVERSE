from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__, template_folder=".")
app.secret_key = "cineverse_secret_key"

# LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":
            session["logged_in"] = True
            return redirect(url_for("home"))
        else:
            return render_template(
                "login.html",
                error="Invalid username or password!"
            )

    return render_template("login.html")


# HOME PAGE
@app.route("/")
def home():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    return render_template("index.html")


# BOOKING PAGE
@app.route("/booking")
def booking():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    return render_template("booking.html")


# PAYMENT PAGE
@app.route("/payment")
def payment():
    if "logged_in" not in session:
        return redirect(url_for("login"))

    return render_template("payment.html")


# LOGOUT
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
