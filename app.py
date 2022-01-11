from flask import Flask, render_template


app = Flask("")


@app.route('/')
def index():
    return "hello world"


@app.route('/table')
def table():
    # return "asghar"
    return render_template('table.html', users=1)

@app.route('/login')
def login():
    return render_template('login.html', users=1)

if __name__ == "__main__":
    app.run()
