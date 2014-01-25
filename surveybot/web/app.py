from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/survey", methods=['POST', 'GET'])
def survey():
    currentPage = request.args.get('currentPage', '0')
    nextPage = request.args.get('nextPage', '1')
    return render_template('survey.html', currentPage=currentPage, nextPage=nextPage)

if __name__ == "__main__":
    app.run()
