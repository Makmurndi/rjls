from flask import Flask, render_template, redirect, url_for
import random

app = Flask(__name__)

# Daftar simbol mahjong
symbols = ["🀄", "🃏", "🀊", "🀋", "🀌", "🀍", "🀎", "🀏"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spin')
def spin():
    results = random.choices(symbols, k=3)  # Mengambil 3 simbol secara acak
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)