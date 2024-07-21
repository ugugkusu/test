from flask import Flask, render_template, request, make_response, flash
import secrets

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'



@app.route("/create-new-post")
def index():
    return secrets.token_hex(64)