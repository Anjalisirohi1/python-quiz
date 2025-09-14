import random
from question_model import Question
from question_data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    ques_text = question["text"]
    ques_opt = question["options"]
    ques_ans = question["answer"]
    new_question =Question(ques_text,ques_opt,ques_ans)
    question_bank.append(new_question)

random.shuffle(question_bank)
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"Quiz over! Final score:{quiz.score}/{len(question_bank)}")
