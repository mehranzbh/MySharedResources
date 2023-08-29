from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/')
def get_random_number():
    return jsonify({
        'random_number': random.randint(1, 100)  # This returns a random number between 1 and 100
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
