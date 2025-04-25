# python_quiz_app.py

def welcome():
    print("🐍 Welcome to the Python CLI Quiz App!")
    name = input("Enter your name: ")
    print(f"\nHello {name}! Let's test your Python knowledge.\n")
    return name

def get_questions():
    return [
        {
            "question": "What is the output of: print(type([]))?",
            "options": ["A. <class 'list'>", "B. <class 'dict'>", "C. <class 'tuple'>", "D. <class 'set'>"],
            "answer": "A"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. func"],
            "answer": "C"
        },
        {
            "question": "Which of the following is a Python tuple?",
            "options": ["A. [1, 2, 3]", "B. {1, 2, 3}", "C. (1, 2, 3)", "D. <1, 2, 3>"],
            "answer": "C"
        },
        {
            "question": "What does the len() function do?",
            "options": ["A. Returns the length", "B. Finds error", "C. Converts to string", "D. Exits program"],
            "answer": "A"
        },
        {
            "question": "Which of these is NOT a Python data type?",
            "options": ["A. int", "B. float", "C. real", "D. bool"],
            "answer": "C"
        }
    ]

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['question']}")
        for option in q["options"]:
            print(option)
        answer = input("Your answer (A/B/C/D): ").strip().upper()
        if answer == q["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is {q['answer']}")
    return score

def show_result(name, score, total):
    print("\n🎉 Quiz Completed!")
    print(f"{name}, your final score is: {score} out of {total}")
    if score == total:
        print("🏆 Excellent! You're a Python pro!")
    elif score >= total / 2:
        print("👍 Good job! Keep practicing.")
    else:
        print("📘 Don't worry! Practice makes perfect.")

def main():
    name = welcome()
    questions = get_questions()
    score = run_quiz(questions)
    show_result(name, score, len(questions))

if __name__ == "__main__":
    main()
