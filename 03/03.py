from flask import Flask,render_template

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<87>')
def hello(name=None):
    return render_template('index.html', name=name)

if __name__ =="__main__":
    app.run()