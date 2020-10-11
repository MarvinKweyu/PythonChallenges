"""
Author:
Date created:
Date last changed:

A Program to allow creation of questions and multiple choice answers together with their difficulty
Input: data.txt
"""

import json

DATA = None

try:
    # read file in read mode
    with open("data.txt", 'r') as f:
        DATA = json.load(f)
except FileNotFoundError:
    DATA = []

def inputInt(iPrompt):
    """Repeatedly prompts for input until an integer is entered."""
    try:
        iPrompt = int(iPrompt)
        return iPrompt
    except:
        while type(iPrompt) != int or iPrompt < 0:
            iPrompt = input('Enter valid integer: ')
            inputInt(iPrompt)


def inputSomething(sPrompt):
    """Repeatedly prompts for input until something other than whitespace is entered."""
    # remove all white spaces from input and check that it is still has content
    while len(sPrompt.strip()) == 0:
        sPrompt = input('Enter valid input: ')
        inputSomething(sPrompt)
    return sPrompt


def save(listDataList):
    """open "data.txt" in write mode and write the data to it in JSON format."""
    DATA.append(listDataList)
    with open("data.txt", 'w') as f:
        json.dump(DATA, f, indent=2)


def inputQuestionAnswers():
    """Accept multiple choice answers """
    listallAnswers = []
    squestionAnswer = None
    while squestionAnswer != "q":
        sAnswer = input('Enter a valid answer (enter "q" when done): ').lower()
        squestionAnswer = inputSomething(sAnswer)
        listallAnswers.append(squestionAnswer.lower())

    if len(listallAnswers) < 1:
        inputQuestionAnswers()
    listallAnswers.remove("q")
    return listallAnswers


def inputQuestionDifficulty():
    ilevel = 0
    idifficulty = int(input('Enter question difficulty (1-5): '))

    while type(idifficulty) != int:
        idifficulty = int(input('Enter question difficulty (1-5): '))

    if idifficulty < 1 or idifficulty > 5:
        inputQuestionDifficulty()
    else:
        ilevel = inputInt(idifficulty)
    return ilevel


def calculateMarks(iDifficulty):
    return iDifficulty * 2

def additionOfQuestion(sNewQuestion = None, sQuestionAnswers = None, sQuestionDifficulty = None):
    """
    Add a new question
    :param squestion:
    :param sNewQuestion:
    :param sQuestionAnswers:
    :param sQuestionDifficulty:
    :return None
    """
    dictNewData = {}
    sQuestionMarks = 0

    if not sNewQuestion or not sQuestionAnswers or not sQuestionDifficulty:
        squestion = input('Enter the question: ')
        sNewQuestion = inputSomething(squestion)
        sQuestionAnswers = inputQuestionAnswers()
        sQuestionDifficulty = inputQuestionDifficulty()
        sQuestionMarks = calculateMarks(sQuestionDifficulty)
    else:
        sQuestionMarks = calculateMarks(sQuestionDifficulty)
    dictNewData['question'] = sNewQuestion
    dictNewData['answers'] = sQuestionAnswers
    dictNewData['difficulty'] = sQuestionDifficulty
    dictNewData['marks'] = sQuestionMarks
    save(dictNewData)
    print("Question added!")

def listOfQuestions():
    # List the current questions.
    if not DATA:
        print("No questions saved")
    else:
        print("Current questions")
        for index, question in enumerate(DATA):
            print(f"{index} ) {question['question']}")

def search():
    # Search the current questions.
    if not DATA:
        print("No questions saved")
    else:
        iprompt = input('Enter a search term: ')
        iSearchTerm = inputSomething(iprompt)
        print("Search results: ")
        for index, question in enumerate(DATA):
            if iSearchTerm in question['question'].lower():
                print(f"\t{index} ) {question['question']}")

def viewQuestionDetail():
    iprompt = input('Question number to view: ')
    iQuestionNumber = inputInt(iprompt)
    sQuestionDetail = ""
    if not DATA:
        print("No questions saved")
    try:
        # DATA[iQuestionNumber]
        for index, question in enumerate(DATA):
            if index == iQuestionNumber:
                sQuestionDetail = f""" 
                    \nQuestion:\n\t{question['question']}
                     \nValid answers: {', '.join(question['answers'])}
                    \nDifficulty: {question['difficulty']}
                    \nMarks awarded: {question['marks']}
                """
    except:
        sQuestionDetail = "Invalid index number"
    return sQuestionDetail

def delete():
    # Delete a question.
    if not DATA:
        print("No questions saved")
    else:
        iPrompt = input('Question number to delete: ')
        iQuestionNumber = inputInt(iPrompt)
        try:
            DATA[iQuestionNumber]
            DATA.pop(iQuestionNumber)
            save(DATA)
            print("Question deleted!")
        except:
            print("Invalid index number")

def empty():
    if len(DATA) > 0:
        return True
    else:
        return False

def main():
    print('Welcome to the Quiz Admin Program.')

    while True:
        print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
        sChoice = input('> ')

        if sChoice == 'a':
           additionOfQuestion()
        elif sChoice == 'l':
            listOfQuestions()

        elif sChoice == 's':
            search()

        elif sChoice == 'v':
            print(viewQuestionDetail())

        elif sChoice == 'd':
            delete()

        elif sChoice == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid sChoice")


if __name__ == "__main__":
    main()
