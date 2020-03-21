import flask
from classes import process_email
from flask import request, jsonify, render_template

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def index():
    return render_template('email_form.html')

#This endpoint is used as the form action from the front end form.
@app.route('/api/v1/email/send', methods=['POST'])
def proc_email():
    if request.form:
        email = process_email.Process(request.form)
        return email.response()

app.run()
