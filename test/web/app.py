from flask import Flask, render_template, request

app = Flask(__name__)

body = ''

@app.route("/")
def index():
    return render_template('index.html', body=body)

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'

if __name__ == "__main__":
    app.run()
