from flask import Flask, render_template, request, redirect, url_for
from wordsolver import WordFinder

app = Flask(__name__)
app.config.from_pyfile(f'{app.root_path}/config_defaults.py')


@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Docstring
    """
    if request.method == 'POST':
        letters = request.form['letters']
        return redirect(url_for('results', letters=letters))
    return render_template('index.html')


@app.route('/results/<letters>')
def results(letters):
    """
    Docstring
    """
    Finder = WordFinder()
    result = Finder.search(letters)
    print(result)
    return render_template('results.html', letters=letters, results=result)


if __name__ == '__main__':
    app.run(debug=True)
