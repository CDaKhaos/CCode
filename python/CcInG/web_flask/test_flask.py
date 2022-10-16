from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("./login.html")


@app.route('/success_get/<name>')
def success_get(name):
    return 'get welcome %s' % name


@app.route('/success_post/<name>')
def success_post(name):
    return 'post welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        print(1)
        user = request.form['nm']
        return redirect(url_for('success_post', name=user))
    else:
        print(2)
        user = request.args.get('nm')
        return redirect(url_for('success_get', name=user))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
