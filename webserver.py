#create a webservice using flask framework

#import all the required modules
from flask import Flask, render_template, request, redirect, url_for, jsonify

#uses css for styling
#uses a black background and white text
#background is smooth texture
#uses a comic sans font
#html string for the web page
#provides a form where user can enter username and password
#provides a submit button
#provides a link to the register page
#provides a link to the login page
html = '''
<!DOCTYPE html>
<html>
<head>
<title>Web Server</title>
<style>
body {
background-image: url("https://i.imgur.com/3gBGf1b.jpg");
background-repeat: no-repeat;
background-size: cover;
p {
    color: red;
}
color: white;
font-family: "Comic Sans MS", cursive, sans-serif;
}
</style>
</head>
<body>
<h1>Web Server</h1>
<form action="/login" method="post">
<label for="username">Username:</label>
<input type="text" id="username" name="username">
<label for="password">Password:</label>
<input type="password" id="password" name="password">
<input type="submit" value="Submit">
</form>
<p><a href="/register">Register</a></p>
<p><a href="/login">Login</a></p>
</body>
</html>

'''
#create an instance of flask
app = Flask(__name__)
#create a simple endpoint
#just return a string
@app.route('/')
def index():
    return html
    return 'Hello World!'


#run the webserver
if __name__ == '__main__':
    app.run(debug=True)





