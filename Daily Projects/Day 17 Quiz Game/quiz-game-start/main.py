import data
import question_model
import quiz_brain

question_bank = []
for i in range(len(data.open_tbd)):
    question = question_model.Question(data.open_tbd[i]["question"], data.open_tbd[i]["correct_answer"])
    question_bank.append(question)

quiz_controller = quiz_brain.QuizBrain(question_bank)
while quiz_controller.has_questions_remaining():
    question = quiz_controller.next_question()

print("Thank you for playing!")
print(f"Your final score is {quiz_controller.score} out of {len(question_bank)}.")