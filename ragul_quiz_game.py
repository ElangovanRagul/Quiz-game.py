
import tkinter as tk
from tkinter import messagebox
import random

# List of questions with options and answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "answer": "Mars"},
    {"question": "Who wrote 'Hamlet'?", "options": ["Shakespeare", "Hemingway", "Twain", "Dickens"], "answer": "Shakespeare"},
    {"question": "What is the smallest prime number?", "options": ["1", "2", "3", "5"], "answer": "2"},
    {"question": "Which ocean is the largest?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "answer": "Pacific"}
]
random.shuffle(questions)

class SignInPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign In")

        self.label = tk.Label(root, text="Enter your name:")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Start Quiz", command=self.start_quiz)
        self.button.pack()

    def start_quiz(self):
        player_name = self.entry.get()
        if player_name:
            self.root.destroy()
            quiz = Quiz(player_name)
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

class Quiz:
    def __init__(self, player_name):
        self.root = tk.Tk()
        self.root.title("Quiz Game")
        self.score = 0
        self.current_question = 0
        self.player_name = player_name

        self.label_name = tk.Label(self.root, text=f"Player: {self.player_name}")
        self.label_name.pack()

        self.label_score = tk.Label(self.root, text=f"Score: {self.score}")
        self.label_score.pack()

        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack()

        self.options = []
        for i in range(4):
            btn = tk.Button(self.root, text="", command=lambda i=i: self.check_answer(i))
            btn.pack()
            self.options.append(btn)

        self.next_question()

        self.root.mainloop()

    def next_question(self):
        if self.current_question < len(questions):
            question = questions[self.current_question]
            self.question_label.config(text=question["question"])
            for i, option in enumerate(question["options"]):
                self.options[i].config(text=option)
        else:
            messagebox.showinfo("Quiz Completed", f"Your final score is: {self.score}")
            self.root.destroy()

    def check_answer(self, selected_index):
        question = questions[self.current_question]
        selected_option = question["options"][selected_index]
        if selected_option == question["answer"]:
            self.score += 1
            self.label_score.config(text=f"Score: {self.score}")
        self.current_question += 1
        self.next_question()

if __name__ == "__main__":
    root = tk.Tk()
    sign_in = SignInPage(root)
    root.mainloop()
