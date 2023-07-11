from flask import Flask, jsonify, request

app = Flask(__name__)

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    n = int(request.args.get('n', 0))
    result = fibonacci(n)
    return jsonify({'fibonacci': result})

if __name__ == '__main__':
    app.run()