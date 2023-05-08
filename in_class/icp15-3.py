# Iris Canavan, Section 3

from flask import Flask, request

app = Flask(__name__)

strHTML_top = "<!DOCTYPE html><html><head><body>"
strHTML_bottom = "</body></html>"

@app.route("/")
@app.route("/home")
def fHome():
	strHTML = strHTML_top + "<h1>This is the home page!</h1>" + strHTML_bottom
	return strHTML

@app.route("/form")
def frmRegister():
	strForm = """
	<!DOCTYPE HTML>
	<html>
		<head>
			<meta charset = "UTF-8">
			<title>Input Controls</title>
			<meta name = "description" content = "form input controls">
			<meta name = "keywords" content = "html sample page">
		</head>
		<body>
			<h1>Register</h1>
			<hr />
				<form action = "/register" method = "post">
					First Name: <input type = "text" name = "fName" placeholder = "Enter first name" required/>
					<br />
					Last Name: <input type = "text" name = "lName" placeholder = "Enter last name" required/>
					<br />
					Email: <input type = "text" name = "email" placeholder = "Enter email address" required/>
					<hr />
					<input type = "submit" value = "Register">
				</form>
		</body>
	<html>"""
	return strForm

@app.route("/register", methods = ["GET", "POST"])
def fRegister():
	first = request.form.get("fName")
	last = request.form.get("lName")
	email = request.form.get("email")
	if first is None:
	  first = ""

	if last is None:
	  last = ""

	return ("<h1>Thank you for Registering</h1>" + first + " " + last + "<br /><br />" + email)

if __name__ == "__main__":
	app.run(host = "127.0.0.1", port = 4000, debug = True)
