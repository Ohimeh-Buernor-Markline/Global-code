def while_loop():
    i = 6
    while(i > 5 and i <19 ):
        i = i+1
        print (i)
while_loop()

print("--------------------------------")
print(" ")

def even():
    for j in range(12,20,2):
        print(j)
        
even()

print("--------------------------------")
print(" ")


def asterix():
    for i in range(4):
        print("****")
asterix()

print("--------------------------------")
print(" ")

def increm():
    for i in("*","**","***","****"):
        print(i)
    for j in("***","**","*"):
        print(j)
increm()

def evenOdd():
    num = int(input("Enter a whole number here: "))
    if (num>0 % 2 == 0):
        print ("Even number")
    elif (num>0 % 2 == 1):
        print("Odd number")
    elif (num == 0):
        print ("You entered 0 / zero")
    else:
        print("Enter a number greater than 0 / zero")
        
evenOdd()

print("--------------------------------")
print(" ")

def calculate():
    num1 = int(input("Enter a whole number here: "))
    num2 = int(input("Enter another whole number here: "))
    operator = str.lower(input("Enter an operator here(eg.add, subtract, etc): "))
    if (operator == "add"):
        results = num1 + num2
        print(num1, " + ", num2, " = ", results)
    elif (operator == "subtract"):
        results = num1 - num2
        print(num1, " - ", num2, " = ", results)
    elif (operator == "multiply"):
        results = num1*num2
        print(num1, " x ", num2, " = ", results)
    elif (operator == "divide"):
        results = num1/num2
        print(num1, " / ", num2, " = ", results)
    else:
        print("Your command was not recognised")



print("--------------------------------")
print(" ")

def lists():
    list = []
    list.append(a)
    print (list)
lists()