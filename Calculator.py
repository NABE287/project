#Describe operators
operators = ["+", "-", "*", "/"]


# Create Calculator Class
class Calculator:
    def __init__(self, FirstNumber, SecondNumber):
        self.FirstNumber = FirstNumber
        self.SecondNumber = SecondNumber

# Function that stores operations on numbers and assumes impossibility of dividing by zero
        
    def operation(self):
        while True:
            try:
                operator = input("Please enter the operator: ")
                if operator == "+":
                    return f"Result is {self.FirstNumber + self.SecondNumber}"
                elif operator == "-":
                    return f"Result is {self.FirstNumber - self.SecondNumber}"
                elif operator == "*":
                    return f"Result is {self.FirstNumber * self.SecondNumber}"
                elif operator == "/":
                    return f"Result is {self.FirstNumber / self.SecondNumber}"
                else:
                    print("Please, input correct operator!")
            except ZeroDivisionError:
                return "Impossible to devide by zero!"
            
#Function that allows to enter  only integer or float numbers
            
def numbers():
    while True:
        try:
            # Asking user to input first number
            num1 = input("Please, input number 1: ")
            num1 = float(num1)
            break
        except:
            print("Input only integers or floats!")
        
    while True:
        try:
            # Asking user ti input second number
            num2 = input("Please, input number 2: ")
            num2= float(num2)

            break
        except:
            print("Input only integers or floats!")

    return num1, num2

while True:
    
    print(f"List of available operators:\n{operators}")

    x, y = numbers()

    #Create calculations example by Calculator class
    calculations  = Calculator(x, y)

    result = calculations.operation()

    print(result)
    
    #After function ends, ask user wants to  use calculator agan or not
    
    action = input("Do you want to calculate again? y/n ")

    if action != "y":
        print ("Goodbye :)")
        break