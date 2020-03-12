from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "This is the Index Page ^^"

@app.route("/test_route")
def troll():
    message = "This a test to validate flask behaviour."
    return message

if __name__ == '__main__':
    context = ('search-morty.crt', 'search-morty.key')
    app.run(debug=True, ssl_context=context)
