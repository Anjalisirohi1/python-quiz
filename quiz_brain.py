class QuizBrain:
    def __init__(self,ques_list):
        self.q_num = 0
        self.score = 0
        self.q_list = ques_list

    def still_has_questions(self):
        return self.q_num < len(self.q_list)


    def next_question(self):
        current_ques = self.q_list[self.q_num]
        print(f"Q.{self.q_num + 1}: {current_ques.ques}")
        for idx in range(len(current_ques.opt)):
            print(f"{idx + 1}.{current_ques.opt[idx]}")
        user_ans = input("Choose your option:")
        self.check_answer(user_ans,current_ques.ans)
        self.q_num += 1

    def check_answer(self,user_ans,ans):
        if str(user_ans).lower() == str(ans).lower():
            self.score += 1
            print(f"Correct! Score: {self.score}")
        else:
            print(f"Wrong! Score: {self.score}")
        print(f"The correct answer is:{ans}")