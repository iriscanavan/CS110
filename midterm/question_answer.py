# Iris Canavan, Section 3

N_PASSED = 7

def main():
	correct_answers = ["A", "C", "A", "A", "D", "C", "B", "A", "D", "B"]
	student_answers1 = ["A", "D", "A", "B", "D", "C", "C", "A", "D", "B"]
	student_answers2 = ["A", "B", "A", "C", "A", "C", "D", "B", "D", "B"]

	fcompare_answers(correct_answers, student_answers1)
	fcompare_answers(correct_answers, student_answers2)


def fcompare_answers(correct_answers, student_answers):
	total_correct = 0
	for i in range(len(correct_answers)):
		if correct_answers[i] == student_answers[i]:
			total_correct += 1
	if total_correct >= N_PASSED:
		print("Congratulations! You passed the exam. You have", N_PASSED, "correct answers")
	else:
		print("You failed the exam. You have", total_correct, "correct answers.")

main()

