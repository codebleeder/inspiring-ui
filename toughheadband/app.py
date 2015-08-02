from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# main
if __name__ == '__main__':
    bootstrap = Bootstrap(app)
    app.run(debug=True)



