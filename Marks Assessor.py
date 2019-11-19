#Uses Student’s IT Homework (/25), Assessment (/50) and ICT Final Exam (/100) marks
#Calculates the percentage and overall ICT grade (A/B/C/D/E/F)
#Prints out Student’s name and ICT grade
#This program should be saved in a new file
#Extra: Have each piece of work individually weighted (HW 25%, Assess 35%, Final 40%) to produce their percentage

#Function to validate whether the input is a number
def inputValidHomeworkMark(message):
    while True:
        try:
            userInput = float(input(message))
            if userInput <= 25:
                return userInput
                break
            else:
                print("Please enter a number equal to or below 25 :)")
                continue
        except ValueError:
            print("Please enter a number :)")
            continue
        else:
            return userInput
            break

def inputValidAssessmentMark(message):
    while True:
        try:
            userInput = float(input(message))
            if userInput <= 50:
                return userInput
                break
            else:
                print("Please enter a number equal to or below 50 :)")
                continue
        except ValueError:
            print("Please enter a number :)")
            continue
        else:
            return userInput
            break

def inputValidExamMark(message):
    while True:
        try:
            userInput = float(input(message))
            if userInput <= 100:
                return userInput
                break
            else:
                print("Please enter a number equal to or below 100 :)")
                continue
        except ValueError:
            print("Please enter a number :)")
            continue
        else:
            return userInput
            break

#Function to validate whether the input is a yes or no
def inputValidContinue(message):
    while True:
            userInput = input(message)
            continue_words = ['Yes', 'No', 'yes', 'no', 'yEs', 'yES', 'YeS', 'YEs', 'yeS', 'YES', 'NO', 'nO']
            if userInput not in continue_words:
                print("Please enter a valid word :)")
            else:
                return userInput
                break

calculator_active = True

while calculator_active:
    name = input('What is your name? ')
    #Get Homework Mark
    HomeworkMark = inputValidHomeworkMark("Please enter your Homework Mark: ")
    #Get Assessment Mark
    AssessmentMark = inputValidAssessmentMark("Please enter your Assessment Mark: ")
    #Get Assessment Mark
    ExamMark = inputValidExamMark("Please enter your Exam Mark: ")
    #Get overall grades and percentage
    TotalMark = HomeworkMark + AssessmentMark + ExamMark
    percentage = TotalMark * 100 / 175

#Extra: Have each piece of work individually weighted (HW 25%, Assess 35%, Final 40%) to produce their percentage

    HWweight = HomeworkMark * 100 * 0.25 / 25 
    AMNTweight = AssessmentMark * 100 * 0.35 / 50
    EXweight = ExamMark * 100 * 0.4 / 100
    WeightedMark = HWweight + AMNTweight + EXweight

    #Print the output as required
    if WeightedMark >= 90:
        print('Student: {0}, Grade: A'.format(name))
    elif WeightedMark >= 80:
        print('Student: {0}, Grade: B'.format(name))
    elif WeightedMark >= 70:
        print('Student: {0}, Grade: C'.format(name))
    elif WeightedMark >= 60:
        print('Student: {0}, Grade: D'.format(name))
    elif WeightedMark >= 50:
        print('Student: {0}, Grade: E'.format(name))
    else:
        print('Student: {0}, Grade: F'.format(name))

    #Ask whether the user wants to continue
    #Stop or continue based on input
    userchoice = inputValidContinue('Do you want to continue, Yes or No? ')

    if userchoice == 'No' or userchoice == 'nO' or userchoice == 'NO' or userchoice == 'no':
        calculator_active = False
        break

