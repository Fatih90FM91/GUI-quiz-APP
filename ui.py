from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0
        self.window = Tk()
        self.window.title('Quiz App')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Ariel', 20, 'italic'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg='white')
        self.question_text = self.canvas.create_text(150, 125, width=280, text='Some questions..', fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_Img = PhotoImage(file='images/true.png')

        self.check_Btn = Button(image=true_Img, pady=20, highlightthickness=0, command=self.true_btn_pressed)
        self.check_Btn.grid(row=2, column=0)

        false_Img = PhotoImage(file='images/false.png')
        self.false_Btn = Button(image=false_Img, pady=20, highlightthickness=0, command=self.false_btn_pressed)
        self.false_Btn.grid(row=2, column=1)

        self.get_next_question()



        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)

        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the limit of the Questions!!')
            self.check_Btn.config(state='disabled')
            self.false_Btn.config(state='disabled')




    def true_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_btn_pressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score += 1
            self.score_label.config(text=f'Score: {self.score}')

        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)

