# Name:  
# Student Number:  

import json


def input_int(prompt):
    """
    Repeatedly prompts for input until an integer is entered.
    :return int
    """
    try:
        prompt = int(prompt)
        return prompt
    except ValueError:
        while type(prompt) != int or prompt < 0:
            prompt = input('Enter valid integer: ')
            input_int(prompt)


def input_something(prompt: str):
    """
    Repeatedly prompts for input until something other than whitespace is entered.
    :return str
    """
    # remove all white spaces from input and check that it is still has content
    while len(prompt.strip()) == 0:
        prompt = input('Enter valid input: ')
        input_something(prompt)
    return prompt


def save_data(data_list):
    """
    open "data.txt" in write mode and write the data to it in JSON format.
    :return none
    """
    overwrite_data = []
    overwrite_data.append(data_list)
    with open("data.txt", 'w') as output_file:
        json.dump(overwrite_data, output_file, indent=2)


def input_question_answers():
    """
    Accept multiple choice answers
    :return list()
    """
    all_answers = []
    question_answer = None
    while question_answer != "q":
        answer = input('Enter a valid answer (enter "q" when done): ').lower()
        question_answer = input_something(answer)
        all_answers.append(question_answer.lower())

    if len(all_answers) < 1:
        input_question_answers()
    all_answers.remove("q")
    return all_answers


def input_question_difficulty():
    """
    Enter question difficulty level
    :return int
    """
    level = None
    difficulty = int(input('Enter question difficulty (1-5): '))

    while type(difficulty) != int:
        # make sure difficulty is entered as an int
        difficulty = int(input('Enter question difficulty (1-5): '))

    if difficulty < 1 or difficulty > 5:
        input_question_difficulty()
    else:
        level = input_int(difficulty)
    return level


data = None

try:
    # read file in read mode
    with open("data.txt", 'r') as f:
        data = json.load(f)
except FileNotFoundError:
    data = []

print('Welcome to the Quiz Admin Program.')

while True:
    print('\nChoose [a]dd, [l]ist, [s]earch, [v]iew, [d]elete or [q]uit.')
    choice = input('> ')

    if choice == 'a':
        new_data = {}
        # Add a new question.
        question = input('Enter the question: ')
        new_question = input_something(question)
        question_answers = input_question_answers()
        question_difficulty = input_question_difficulty()

        new_data['question'] = new_question
        new_data['answers'] = question_answers
        new_data['difficulty'] = question_difficulty
        save_data(new_data)
        print("Question added!")

    elif choice == 'l':
        # List the current questions.
        if not data:  # if no questions are available, print
            print("No questions saved")
        else:
            print("Current questions")
            for index, question in enumerate(data):
                print(f"{index} ) {question['question']}")

    elif choice == 's':
        # Search the current questions.
        if not data:
            print("No questions saved")
        else:
            prompt = input('Enter a search term: ')
            search_term = input_something(prompt)
            print("Search results: ")
            for index, question in enumerate(data):
                if search_term in question['question'].lower():
                    print(f"\t{index} ) {question['question']}")

    elif choice == 'v':
        prompt = input('Question number to view: ')
        question_number = input_int(prompt)
        if not data:
            print("No questions saved")
        try:
            print(f"\nQuestion:\n\t{data[question_number]['question']}")
            print(f"\nValid answers: {', '.join(data[question_number]['answers'])}")
            print(f"Difficulty: {data[question_number]['difficulty']}")
        except IndexError:
            print("Invalid index number")

    elif choice == 'd':
        # Delete a question.
        if not data:
            print("No questions saved")
        else:
            prompt = input('Question number to delete: ')
            question_number = input_int(prompt)
            try:
                # remove the question from the array using pop
                data.pop(question_number)
                save_data(data)
                print("Question deleted!")
            except IndexError:
                print("Invalid index number")

    elif choice == 'q':
        print("Goodbye!")
        break

    else:
        print("Invalid choice")
