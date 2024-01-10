from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def welcome_page():
    title = "WELCOME"
    return render_template('welcome/welcome.html', title=title)

@app.route('/dashboard')
def main():
    title = "LETS START"
    return title

if __name__ == "__main__":
    app.run(debug=True)
