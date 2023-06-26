from flask import Flask, render_template, redirect, request, url_for
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.secret_key = '123'
app.debug = True

toolbar = DebugToolbarExtension(app)




@app.route('/', methods=['POST','GET'])
def index():
    return render_template('index.html')


@app.route('/game', methods = ['POST','GET'])
def game():
    lives = request.args.get('lives')
    categories = request.args.get('categories')
    if request.method == 'POST':
        lives = request.form['lives']
        username = request.form['username']
        categories = request.form['categories']
        return redirect(url_for('play', username=username,lives=lives, categories=categories))
    return render_template('charSelect.html', lives=lives, categories=categories)

@app.route('/game/<username>', methods=['POST', 'GET'])
def play(username):
    lives = request.args.get('lives')
    categories = request.args.get('categories')
    if username == None:
        return render_template('charSelect.html')
    return render_template('game.html', username=username, lives=lives, categories=categories)

@app.route('/option', methods=['POST','GET'])
def option():
    if request.method == 'POST':
        lives = request.form['lives']
        categories = request.form['categories']
        return redirect(url_for('game', lives=lives, categories=categories))
        

    return render_template('option.html')
    


    


@app.route('/about')
def about():
    return render_template('about.html')

if '__main__' == __name__:
    app.run()


