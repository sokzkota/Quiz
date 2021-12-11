import random
from data import  question_data
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

# q1 = Question(question_data[0]["text"], question_data[0]["answer"])
# print(q1.text)
# print(q1.answer)