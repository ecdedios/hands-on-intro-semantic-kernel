import prompter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def prompt():
    prompt = request.form['prompt']
    response = prompter.chatgpt(prompt)
    return render_template('/submit.html',
                           prompt = prompt,
                           response = response)

