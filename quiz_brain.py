# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end of the quiz


class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.final_score = 0
        self.question_list = q_list


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.q_text} (True/False):  ")
        self.check_answer(user_ans, current_question.q_answer)

# ------------Basic return------
    # def still_has_question(self):
    #     if self.question_number < len(self.question_list):
    #         return True
    #     else:
    #         False

    # --------advance return--------
    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got is right!!")
        else:
            print("That's wrong!!")
        print(f"The correct answer was: {correct_answer}")
        print(f"You current score is {self.score}/{self.question_number}\n")
