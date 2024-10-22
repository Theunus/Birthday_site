from flask import Flask, render_template
import os

# Adjust the template_folder path
app = Flask(__name__, template_folder=os.path.join('app', 'templates'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/funny')
def funny():
    return render_template('funny.html')

if __name__ == '__main__':
    app.run(debug=True)
