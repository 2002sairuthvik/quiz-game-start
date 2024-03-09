class QuizBrain():
    
    def __init__(self,q_list):
        self.qnumber = 0
        self.qlist = q_list
        self.score = 0
        
    
    def still_has_questions(self):
        if self.qnumber < len(self.qlist):
            return True
        else:
            print("You've Completed the quiz")
            print(f"The Final Score is {self.score} / {self.qnumber}")
            return False
    
    def next_question(self):
        current_question = self.qlist[self.qnumber]
        self.qnumber+=1
        choice = input(f"Q.{self.qnumber} : {current_question.text} (True/False) :")
        self.check_answer(choice , current_question.answer)
    
    def check_answer(self , choice , correct_ans ):
        if choice.lower() == correct_ans.lower():
            print("You got it right")
            self.score+=1
            
        else:
            print("You got it wrong!")
        print(f"The Correct answer is {correct_ans}.")
        print(f'The Score is {self.score} / {self.qnumber}') 
        print("\n")