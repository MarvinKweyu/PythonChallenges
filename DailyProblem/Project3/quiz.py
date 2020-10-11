# Name:  
# Student Number:  

# You are not required to reference it.

import tkinter
import tkinter.messagebox
import json
import random


class ProgramGUI:

    def __init__(self):
        """loading and reading the data from the text file and creating the user interface."""
    
        self.window = tkinter.Tk()
 
        self.window.title("Quiz") 
        self.window.geometry('550x300')
       
        # read file in read mode
        try:
            with open("project/data.txt", 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            # message box window 
            tkinter.messagebox.showerror("Missing file", "Missing/invalid file")
            self.window.destroy()
            return
            
        if len(self.data) < 5:
            # message box insufficient number of questions.End prog
            tkinter.messagebox.showerror("Low question count", "Insufficient number of questions")
            self.window.destroy()
            return

        self.current_question = 1
        self.score = 0

        self.show_question()
        tkinter.mainloop()
        



    def show_question(self):
        """displaying the current question and some other messages in the GUI."""

        question_count = tkinter.Label(self.window, text = f"Question {self.current_question} of 5")
        question_count.grid (column=4, row=0, columnspan = 7)
        self.question = random.choice(self.data)
        # delete question to avoid duplicates
        self.data.remove(self.question)

        if self.question['difficulty'] >=4:
            self.luck_label = tkinter.Label(self.window, text = f"This is a hard one - good luck!", fg="blue")
            self.luck_label.grid (column=2, row=2, columnspan = 7)

        question_label = tkinter.Label(self.window, text = f"{self.question['question']}")
        question_label.grid (column=2, row=4, columnspan = 7)

        self.answer = tkinter.Entry(self.window,width=20)
        self.answer.focus()
        self.answer.grid(column=3, row=6, columnspan = 3)

        button = tkinter.Button(self.window, text="Submit Answer", command=self.check_answer)
 
        button.grid (column=8, row=6)



    def check_answer(self):
        """check if the user's answer is correct when the button is clicked."""   
        user_answer = self.answer.get()

        if user_answer in self.question['answers']:
            tkinter.messagebox.showinfo("Correct!", "You are correct!")
            self.score += (self.question["difficulty"] * 2)
        else:
            tkinter.messagebox.showerror("Incorrect!", "Sorry, that was incorrect!")
        
        self.current_question +=1

        if self.current_question > 5:
            tkinter.messagebox.showinfo("Final Score", f"Game over.\nFinal score: {self.score}\n\nThank you for playing!")
            self.window.destroy()
            return

        # self.luck_label.place_forget()

        # clear answer field before going to next question
        self.answer.delete(0, 'end')
        self.show_question()
        




# Create an object of the ProgramGUI class to begin the program.
gui = ProgramGUI()

