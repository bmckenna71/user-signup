from flask import Flask, request, redirect, render_template, url_for
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods =["Get"])
def index():
    return render_template("index.html")

@app.route('/', methods= ["GET", "POST"])
def validate():
    username = request.form ["username"]
    username_error =""
    
    if " " in username:
        username_error = "Spaces not permitted"
    elif len(username) <3 or len(username)>20:
        username_error = "Must be 3 - 20 characters"
    else:
        username_error = ""    
    
    password=request.form["password"]
    password_error = ""
    
    if " " in password:
        password_error = "Spaces not permitted"
    elif len(password) <3 or len(password) >20:
        password_error = "Must be between 3 and 20 characters"
    else:
        password_error = ""

    email = request.form["email"]
    email_error = ""

    if email != "":
        if "@" not in email or "@@" in email or "." not in email or ".." in email or " " in email:
            email_error = "Email submission is optional, but must be a valid email address for submission"
        elif len(email)<3 or len(email)>20:
                email_error = "Must be between 3 and 20 characters"
        else:
            email_error = ""

    verify = request.form["verify"]
    verify_error = ""

    if password != verify:
        verify_error = "Passwords must match"
    else:
        verify_error = ""
  
    if not username_error and not verify_error and not password_error and not email_error:
        return redirect (url_for("welcome", username = username))
    else:
        return render_template ("index.html", username = username, username_error = username_error, password_error = password_error, verify_error = verify_error, email = email, email_error = email_error)

@app.route("/welcome")
def welcome():
    username = request.args.get("username")
    return render_template("welcome.html", username = username)


   
app.run()