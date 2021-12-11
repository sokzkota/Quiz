class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score = 0
        self.answer = ""

    def still_has_questions(self):
        return len(self.question_list) > self.question_number

    @property
    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        self.answer = input(f"Q.{self.question_number}: {question} (True/False)")

        return self.question_number

    def check_answer(self):
        q_answer = self.question_list[self.question_number-1].answer

        if self.answer.lower() == q_answer.lower():
            self.user_score += 1
            print("That's Right")
        else:
            print("That's Wrong")
            # print(f"Question Answer was {q_answer}")
        print(f"Question Answer was {q_answer}")
        print(f"Your current score is {self.user_score}/{self.question_number}")
        print("\n\n")
        return self.user_score


