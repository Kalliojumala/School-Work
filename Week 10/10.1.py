#'game' that asks the user list 5 of the first 20 elements from the periodic table
#gives feedback to the user based on correct answers

def get_answers():
    #read answers from file to list and return it
    answers = []
    with open('alkuaineet.txt', 'r') as file_1:
        for line in file_1:
            answers.append(line.replace('\n', ''))
        file_1.close()
    
    return answers

def user_input():
    #read user input until there is 5 items in the list return it
    answers = []
    while len(answers) < 5:
        user_input = input(f"Syötä aine {len(answers)+1}: ")
        #check for duplicates, if input already in list ask again without adding the dup 
        if user_input.lower() in answers:
            print(f"{user_input.lower()} on jo syötetty. Duplikaatit eivät ole sallittuja!")
        if user_input.lower() not in answers: 
            answers.append(user_input.lower())

    return answers

def check_answers(user_answers: list, correct_answers: list):
    correct_dict = {'Oikein': [], 'Väärin': []}
    for item in user_answers:
        if item in correct_answers:
            correct_dict['Oikein'].append(item)
        else:
            correct_dict['Väärin'].append(item)

    return correct_dict

def format_output(user_score: dict):
    #calculate percentage of correct answers
    correct_percentage = len(user_score['Oikein']) / (len(user_score['Oikein'])+len(user_score['Väärin'])) * 100

    #format correct and incorrect answers to string 
    correct_string = ", ".join(user_score['Oikein'])
    incorrect_string = ", ".join(user_score['Väärin'])

    #assign rank based on correct answers
    if correct_percentage < 41:
        rank = 'Noob'
    elif correct_percentage < 75:
        rank = 'Average'
    else:
        rank = 'Good'

    #return string to print out, add the three created variables together for data in a easy to read form
    return f"\n{correct_percentage}% oikein. Oikein: {correct_string}. Väärin: {incorrect_string}.\nTaitotaso: {rank}"

###MAIN###

#get correct answ
correct = get_answers()

#get user input
print('Kerro viisi ensimmäisistä 20:stä alkuaineesta jaksollisessa järjestelmässä:\n')
user = user_input()

#compare user input to correct answers
user_score = check_answers(user, correct)
print(format_output(user_score))
   

