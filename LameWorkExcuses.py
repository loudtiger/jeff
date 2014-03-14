from bottle import route, run, template
from flask import Flask, g, jsonify, redirect, render_template, request, url_for

import random

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	excuses = []
	with open('excuses.txt') as f:
		for line in f:
			excuses.append(line)
	
	chosenExcuse = random.choice(excuses)
	
	return render_template('index.html', theExcuse=chosenExcuse)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5002)
