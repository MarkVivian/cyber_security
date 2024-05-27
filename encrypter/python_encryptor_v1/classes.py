'''
        CREATION
create a class called calculator
the calculator should:
    a) ADD, SUB, MULT, DIV
    b) the values are passed by the user.
'''

# calculator version 1

'''
class Calculator:
    def __init__(self ,number1, number2):
        self.number1=number1
        self.number2=number2

    def addition(self):
        total= self.number1+self.number2
        print(total)

    def subtraction(self):
        total=self.number1-self.number2
        print(total)

    def multiplication(self):
        total=self.number1*self.number2
        print(total)

    def division(self):
        total=self.number1/self.number2
        print(total)

Calculator(1, 2).addition()
'''


class calculator:
    def __init__(self, num1, num2,operation):
        self.num1 = num1
        self.num2 = num2
        self.geto=operation
        self.operation()

    def operation(self):
        if self.geto==1:
            self.add()
        elif self.geto==2:
            self.div()
        elif self.geto==3:
            self.mult()
        elif self.geto==4:
            self.sub()
        else:
            print("systy not available ")

    def add(self):
        gojo = self.num1 + self.num2
        print(gojo)

    def sub(self):
        gojo = self.num1 - self.num2
        print(gojo)

    def mult(self):
        gojo = self.num1 * self.num2
        print(gojo)

    def div(self):
        gojo = self.num1 / self.num2
        print(gojo)

def user_input():
    num1=input("not today \n")
    num2=input("enter number 2 \n")
    operation = int(input("enter the type of operation "
                          "\n 1) add "
                          "\n 2) subtract "
                          "\n 3) multiplication"
                          "\n 4) division \n value :  "))

    calculator(num1, num2, operation)

# VERSION 2
'''
this version should be able to take user input to predict:
    1) the two values to be worked on
    2) the type of operation to be undertaken on those values.
'''

'''
class Calculator2:
    def __init__(self, number1, number2, operation):
        self.number1 = number1
        self.number2 = number2
        self.chooser(operation)

    def chooser(self, operation):
        if operation == 1:
            self.addition()
        elif operation == 2:
            self.subtraction()
        elif operation == 3:
            self.multiplication()
        elif operation == 4:
            self.division()
        else:
            print(f"operation {operation} selected is not viable.")

    def addition(self):
        total = self.number1 + self.number2
        print(total)

    def subtraction(self):
        total = self.number1 - self.number2
        print(total)

    def multiplication(self):
        total = self.number1 * self.number2
        print(total)

    def division(self):
        total = self.number1 / self.number2
        print(total)


def get_user_input():
    num1 = int(input("enter the number 1: \n"))
    num2 = int(input("enter the number 2: \n"))
    operation = int(input("enter the type of operation "
                          "\n 1) add "
                          "\n 2) subtract "
                          "\n 3) multiplication"
                          "\n 4) division \n value :  "))

    Calculator2(num1, num2, operation)

get_user_input()
'''

