def run_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A) Mumbai", "B) Delhi", "C) Bangalore", "D) Chennai"],
            "answer": "B) Delhi"
        },
        {
            "question": "Who is the current President of the United States?",
            "options": ["A) Joe Biden", "B) Donald Trump", "C) Barack Obama", "D) George Bush"],
            "answer": "B) Donald Trump"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Mars", "C) Jupiter", "D) Saturn"],
            "answer": "C) Jupiter"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["A) H2O", "B) CO2", "C) O2", "D) NaCl"],
            "answer": "A) H2O"
        },
        {
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "options": ["A) William Shakespeare", "B) Charles Dickens", "C) Jane Austen", "D) Mark Twain"],
            "answer": "A) William Shakespeare"
        }
    ]

    score = 0

    for index, q in enumerate(questions):
        print(f"Q{index + 1}: {q["question"]}")
        for option in q["options"]:
            print(option)

        user_answer = input("Your answer: (A/B/C/D): ")
        if user_answer.strip().upper() == q["answer"][0]:
            score += 1

    print(f"Your final score is: {score}/{len(questions)}")

run_quiz()


