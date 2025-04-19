from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message":"Witaj w moim API!"})

@app.route('/mojastrona')
def mojastrona():
    return jsonify({"message":"To jest moja strona!"})

@app.route('/hello', methods=['GET'])
def say_hello():
    name = request.args.get("name", "")
    if name:
        resp = f"Hello {name}"
    else:
        resp = "Hello"
    return jsonify({"message": resp})

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    num1 = float(request.args.get("num1", ""))
    num2 = float(request.args.get("num2", ""))
    sum = num1 + num2
    if sum > 5.8:
        resp = 1 
    else: 
        resp = 0

    return jsonify({"message": resp})

if __name__ == '__main__':
    app.run()
