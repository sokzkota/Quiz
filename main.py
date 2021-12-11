
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import html


question_bank = []
for _ in question_data:
    question = Question(html.unescape(_["question"]), _["correct_answer"])
    # question = html.unescape(_["question"])
    question_bank.append(question)



# print(question_bank[0].answer)
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question
    quiz.check_answer()
print("You have completed the quiz")
print(f"Your final score was {quiz.user_score} / {quiz.question_number}")

 