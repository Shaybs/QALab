#The program is designed to simulate a calculator
#The code starts by defining different functions
#These functions are designed to ensure that valid inputs/responses are
#made by users without the program shutting down
#After which a continuous while loop is used so that the user can decide when
#to exit the application

#Function to validate whether the input is a number
def inputValidNumber(message):
    while True:
        try:
            userInput = float(input(message))
        except ValueError:
            print("Please enter a number :)")
            continue
        else:
            return userInput
            break

#Function to validate whether the input is a mathematical operator
def inputValidOperator(message):
    while True:
            userInput = input(message)
            operator_letters = ['-', '+', '/', '*']
            if userInput not in operator_letters:
                print("Please enter a valid operator :)")
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

#Create a while loop to continuously ask use if they want to continue using the app
calculator_active = True

while calculator_active:
    #Get values
    Value1 = inputValidNumber("Please enter your first number: ")
    Value2 = inputValidNumber("Please enter your second number: ")
    #Get operator
    operator = inputValidOperator("Enter the operator -, +, / or *: ")
    #Get calculation
    subtraction = Value1 - Value2
    addition = Value1 + Value2
    product = Value1 * Value2
    division = Value1 / Value2

    #Print the output as required
    if operator == '-':
        print('{0} - {1} is: {2}'.format(Value1, Value2, subtraction))
    elif operator == '+':
        print('{0} + {1} is: {2}'.format(Value1, Value2, addition))
    elif operator == '*':
        print('{0} * {1} is: {2}'.format(Value1, Value2, product))
    elif operator == '/':
        print('{0} / {1} is: {2}'.format(Value1, Value2, division))

    #Ask whether the user wants to continue
    #Stop or continue based on input
    userchoice = inputValidContinue('Do you want to continue, Yes or No? ')

    if userchoice == 'No' or userchoice == 'nO' or userchoice == 'NO' or userchoice == 'no':
        calculator_active = False
        break

#End
