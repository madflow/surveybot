from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/survey", methods=['POST', 'GET'])
def survey():
    gotoPage = request.args.get('gotoPage', '')
    return render_template('survey.html')

if __name__ == "__main__":
    app.run()
