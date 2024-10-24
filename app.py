from flask import Flask, render_template, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/funny')
def funny():
    return render_template('funny.html')

# Redirect from root URL to home page if accessed incorrectly
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
