from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Flask Application!"

@app.route('/health')
def health():
    return jsonify({"status": "Up & Running"}), 200

@app.route('/about')
def about():
    return jsonify({"message": "This is a simple Flask application."}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run on all available interfaces on port 5000
