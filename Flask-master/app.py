from flask import Flask, render_template, request, url_for
import sys

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("chat.html")

@app.route('/chat/', methods=["POST","GET"])
def chat():
	#t1=request.form['t1']
	#response = chat.chat("hello") #t1)
	return "<h2>test</h2>"#<h2>Bot Response: %s</h2>"%(response)


if __name__ == "__main__":
    app.run()