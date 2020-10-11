"""
Author:
Date created:
Date last changed:

A GUI program to allow creation of questions and multiple choice answers together with their difficulty
Input: data.txt
"""

import tkinter
import tkinter.messagebox
import json
import random

from project import admin

try:
    # read file in read mode
    with open("data.txt", 'r') as f:
        DATA = json.load(f)
except FileNotFoundError:
    DATA = []


def searcheable(window):
    entSearch = tkinter.Entry(window, width=50)
    entSearch.insert(0, 'search')
    entSearch.grid(column=12, row=2, columnspan=3)


def changeMenu(event):
    print("Random")


def newQuestion(entNewQuestion, answer, optMenu):
    print(f"New question: {entNewQuestion.get()}")
    difficulty = optMenu.get()
    admin.additionOfQuestion(entNewQuestion.get(), answer.get(), difficulty)


def layout(window):
    lblMenu = tkinter.Label(window, text=f"Select option")
    lblMenu.grid(column=1, row=0, columnspan=3)

    lstmenuList = tkinter.Listbox(window)
    lstmenuList.insert(1, "List questions")
    lstmenuList.insert(2, "Search question")
    lstmenuList.insert(3, "View question")
    lstmenuList.insert(4, "Delete question")
    lstmenuList.bind('<Double-1>', changeMenu)
    lstmenuList.grid(column=1, row=3, columnspan=3)

    lblNewQuestion = tkinter.Label(window, text=f"New question")
    lblNewQuestion.grid(column=6, row=0, columnspan=3)

    entNewQuestion = tkinter.Entry(window, width=50)
    entNewQuestion.insert(0, 'New question')
    entNewQuestion.grid(column=6, row=3, columnspan=3)

    entAnswer = tkinter.Entry(window, width=50)
    entAnswer.insert(0, 'question answer')
    entAnswer.grid(column=6, row=4, columnspan=3)

    dropVariable = tkinter.StringVar(window)
    dropVariable.set(1)  # default value

    optMenu = tkinter.OptionMenu(window, dropVariable, 1, 2, 3, 4, 5)
    optMenu.grid(column=6, row=5, columnspan=3)

    btnSubmitQuestion = tkinter.Button(window, text="Submit question", command=lambda: newQuestion(entNewQuestion,entAnswer, dropVariable))
    btnSubmitQuestion.grid(column=6, row=6, columnspan=3)

    # frFrame = tkinter.Frame(window)
    lblViewPort = tkinter.Label(window, text=f"View port")
    lblViewPort.grid(column=12, row=0, columnspan=3)
    iuserOption = lstmenuList.get(tkinter.ACTIVE)
    print(iuserOption)
    search = False
    if search:
        searcheable(window)

    entView = tkinter.Entry(window, width=50)
    entView.insert(0, 'result')
    entView.grid(column=12, row=3, columnspan=3)


def main():
    window = tkinter.Tk()

    window.title("Test administration")
    window.geometry('1050x400')
    layout(window)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
