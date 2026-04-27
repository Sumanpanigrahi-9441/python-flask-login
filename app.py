from flask import Flask, request, Response, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "supersecret"

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("user_name")
        password = request.form.get("password")
        
        if username == "sumu" and password == "234":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return "Invalid credentials. Please try again."

    return '''
    <h2>login page</h2>
    <form method="POST">
        username :<input type="text" name="user_name"><br>
        password :<input type="password" name="password"><br>
        <input type="submit" value="submit">
    </form>
    '''

@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
        <h2>Welcome, {session["user"]}!</h2>
        <a href="{url_for('logout')}">Logout</a>
        '''
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
