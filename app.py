from flask import Flask, request, jsonify
app = Flask(__name__)

# Sample quiz questions
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Madrid", "Berlin"],
        "answer": 0
    },
    # Add more questions here...
]

@app.route('/quiz/question/<int:index>', methods=['GET'])
def get_question(index):
    if 0 <= index < len(quiz_questions):
        return jsonify(quiz_questions[index])
    else:
        return jsonify({"error": "Question not found"}), 404

@app.route('/quiz/answer', methods=['POST'])
def check_answer():
    data = request.json
    index = data.get('index')
    selected_option = data.get('selectedOption')
    if 0 <= index < len(quiz_questions):
        correct_answer = quiz_questions[index]['answer']
        is_correct = selected_option == correct_answer
        return jsonify({"isCorrect": is_correct})
    else:
        return jsonify({"error": "Question not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
