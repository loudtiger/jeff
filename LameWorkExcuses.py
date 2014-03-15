from flask import Flask, g, jsonify, redirect, render_template, request, url_for

import random

excuses = []

def init_app():
	with open('excuses.txt') as f:
		for line in f:
			excuses.append(line)

	app = Flask(__name__)
	return app

app = init_app()

@app.route('/', methods=['GET'])
def index():
	chosenExcuse = random.choice(excuses)
	return render_template('index.html', theExcuse=chosenExcuse)
