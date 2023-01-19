from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quizbrain: QuizBrain):
        self.quiz = quizbrain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(bg=THEME_COLOR, fg='white', font=["Arial", 20, 'italic'])
        self.score_label.grid(column=1, row=0)

        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(
            image=true_image,
            pady=20,
            padx=20,
            bg=THEME_COLOR,
            command= self.true_pressed)
        self.true_button.grid(column=0, row=2)
        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(
            image=false_image,
            pady=20,
            padx=20,
            bg=THEME_COLOR,
            command= self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="PlaceHolder",
            font=["Arial", 20, 'italic'],
            fill=THEME_COLOR,
            width=280)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text=f'Score: {self.quiz.score}')
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'Your score was {self.quiz.score}/10')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
