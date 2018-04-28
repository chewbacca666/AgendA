from flask import flask

app = Flask(__name__)

@app.route("/")
def firtapp():
	return"<h1> Ola Como vai voce :D </h1>"

if(__name__ == "__main__"):
	app.run()