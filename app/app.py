from flask import Flask, render_template
import os

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
    # Bind to the PORT environment variable or default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
