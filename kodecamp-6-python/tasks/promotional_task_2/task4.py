# PROMOTIONAL TASK 2 — Task 4: Student Quiz Grader
#
# Requirements:
#   - Answer key: ['A', 'B', 'C', 'A', 'D']  (5 questions)
#   - Function: grade_quiz(student_answers)
#   - Loop: for with range() (or zip) to compare lists
#   - Conditional: match → +20 points, no match → +0
#   - Exception: try/except IndexError if student list is shorter (skipped questions)

answer_key = ["A", "B", "C", "A", "D"]
POINTS_PER_QUESTION = 20


def grade_quiz(student_answers):
    """Grade up to 5 questions. Returns total score out of 100."""
    score = 0

    print("\n" + "=" * 50)
    print("         Student Quiz Results")
    print("=" * 50)
    print(f"  Answer key: {answer_key}")
    print(f"  Student:    {student_answers}\n")

    # LOOP: compare each question (0 to 4)
    for i in range(len(answer_key)):
        correct = answer_key[i]

        try:
            student = student_answers[i]

            # CONDITIONAL: same answer or not
            if student == correct:
                score += POINTS_PER_QUESTION
                print(f"  Q{i + 1}: {student}  |  Correct (+{POINTS_PER_QUESTION})")
            else:
                print(f"  Q{i + 1}: {student}  |  Wrong (answer was {correct}) (+0)")

        except IndexError:
            # Student skipped this question (list too short)
            print(f"  Q{i + 1}: (skipped)  |  No answer (+0)")

    print(f"\n  Final score: {score} / 100\n")
    return score


if __name__ == "__main__":
    print("--- Example A: all 5 answers ---")
    grade_quiz(["A", "C", "C", "A", "D"])

    print("--- Example B: last question skipped ---")
    grade_quiz(["A", "B", "C", "A"])
