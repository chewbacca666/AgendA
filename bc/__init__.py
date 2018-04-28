from flask import Flask

app = Flask(__name__)

@app.route("/")
def firtapp():
	return"<h1> Teta viado </h1><br><br><h2> Lucia pega no meu not KAPPApride </h2>"


if __name__ == "__main__":
	app.run()