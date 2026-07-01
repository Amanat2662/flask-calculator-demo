from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Amanat's Flask Calculator! Use /add?a=5&b=3 or /subtract?a=5&b=3"

@app.route('/add')
def add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"Result: {a + b}"

@app.route('/subtract')
def subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return f"Result: {a - b}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
