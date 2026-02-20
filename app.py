from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# Predefined responses for common mental health topics
responses = {
    "hello": "Hi! I'm your mental health support bot. How are you feeling today?",
    "sad": "I'm here for you. Try taking a few deep breaths and focus on something positive. Would you like some coping techniques?",
    "anxious": "Feeling anxious is tough. Try grounding techniques: 5 things you can see, 4 things you can touch, 3 things you can hear.",
    "stress": "Stress can be overwhelming. Take a short break, stretch, or listen to calming music. Do you want some guided exercises?",
    "depressed": "I'm sorry you're feeling down. Remember, it's okay to seek help. Talking to a friend, journaling, or professional help can help.",
    "help": "If you are in crisis, please contact a trained professional immediately. For example, you can reach out to local hotlines or mental health organizations.",
    "default": "I hear you. Can you tell me more or choose a topic like sad, anxious, stress, or depressed?"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form["message"].lower()
    response = responses.get("default")

    for key in responses:
        if key in user_input:
            response = responses[key]
            break

    return jsonify({"response": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
