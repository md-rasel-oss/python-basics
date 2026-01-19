from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Flask backend is running!"

@app.route("/api/profile")
def profile():
    return jsonify({
        "name": "Md Rasel",
        "role": "Python Learner",
        "goal": "Backend Developer"
    })

if __name__ == "__main__":
    app.run(debug=True)
