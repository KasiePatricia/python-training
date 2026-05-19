# Student Quiz Grader
# Compare student answers to an answer key. 20 points per correct answer.
# Handle shorter student lists safely with try/except.

answer_key = ["A", "B", "C", "A", "D"]


def grade_quiz(student_answers):
    score = 0
    for i in range(len(answer_key)):
        try:
            if student_answers[i] == answer_key[i]:
                score += 20
        except IndexError:
            # Student did not answer this question
            break
    return score


# Example: student skipped the last question
student_answers = ["A", "B", "C", "A"]

result = grade_quiz(student_answers)
total_questions = len(answer_key)
answered = min(len(student_answers), total_questions)

print(f"Answer key:  {answer_key}")
print(f"Student:     {student_answers}")
print(f"Score: {result} / {total_questions * 20} ({result // 20} of {total_questions} correct)")
