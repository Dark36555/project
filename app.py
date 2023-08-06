from flask import Flask, request, jsonify
app = Flask(__name__)

# ... (your existing Flask code) ...

@app.route('/quiz/evaluate', methods=['POST'])
def evaluate_quiz():
    user_answers = request.form

    total_score = 0
    for question_number, correct_answer_index in enumerate(quiz_questions):
        user_answer = user_answers.get(f'q{question_number + 1}')
        if user_answer == quiz_questions[question_number]['options'][correct_answer_index]:
            total_score += 1

    return f"You scored {total_score} out of {len(quiz_questions)}."

# ... (the rest of your Flask code) ...


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
