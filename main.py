from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Challenge---------------
# write a for loop to iterate over the question_data
# Create a Question object from each entry in question_data
# Append each Question object to the question_bank


question_bank = []

for i in question_data:
    ques_text = i['text']
    ques_ans = i['answer']
    new_question = Question(ques_text,ques_ans)
    question_bank.append(new_question)
# print(question_bank) # It ll print location of all data not real data


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()


print("You've completed the quiz")
print(f"Your final score is {quiz.score}/{len(question_data)}")

# After completing this project check the Open trivia DB for more questions



















# print(question_data[0]['text'])
# print(question_data[0]['answer'])

# -------Basic code--------
# a = 0
# is_on = True
# while is_on:
#     ques=(question_data[a]['text'])
#     ans=(question_data[a]['answer'])
#     print(f"Ques: {ques}?")
#     user_ans = input("Enter True or False\n")
#     if a > len(question_data):
#         is_on = False
#     if user_ans == ans:
#         a += 1
#     else:
#         is_on = False