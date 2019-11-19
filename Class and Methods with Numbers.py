class MyClass:
    def calNumbers(self):
        number1 = float(input('Enter first number: '))
        number2 = float(input('Enter second number: '))
        total = number1 + number2
        product = number1 * number2

        if number1 > number2 and number1 > 0:
            print('The sum of {0} and {1} is {2}'.format(number1, number2, total))
        if number1 < number2 and number2 > 0:
            print('The product of {0} and {1} is {2}'.format(number1, number2, product))            
        if number1 == 0:
            return number2
        if number2 == 0:
            return number1
            
