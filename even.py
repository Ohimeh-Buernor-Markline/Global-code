import functools
from functools import reduce
def trial1():
    def is_even(num):
       return num % 2 == 0

    num = [1,56,234,87,4,76,24,69,90,135]

    print(list(filter(is_even, num)))
    
def trial2():
    def is_even(num):
        return num % 2 == 0
    
def trial3():
    num = [1,56,234,87,4,76,24,69,90,135]

    print(list(filter(lambda num:num%2==0, num)))
    print(" ")
    
def trial4():    
    total = reduce(lambda item, running_total: item + running_total, [1, 2, 3, 4, 5])
    print(total)
    print(" ")

def trial5():
    hello = "The quick brown fox jumped over the lazy dog"
    words = hello.split()
    print(words)
    print(list([len(word) for word in words]))

def trial6():
    numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    print(list(filter(lambda numbers:numbers>0, numbers)))

def trial7():
    numbers = [12,54,33,67,24,89,11,24,47]
    print(list(filter(lambda numbers:numbers%2==0,numbers)))

def trial8():
    numbers = [12,54,33,67,24,89,11,24,47]
    print([n for n in numbers if n%2==0])

def trial9():
    list1 = range(1,51)
    print(list(list1))
    print(" ")
    print("Even numbers")
    print("____________")
    print([n for n in list1 if n%2==0])

def trial10():
    list1 = range(1,51)
    print(list(list1))
    print(" ")
    print("Odd numbers")
    print("____________")
    print([n for n in list1 if n%2==1])

#def trial11():
#    i = 0
#    for 
#        capitalize = ("hello", "my", "name", "is", "Markline")
#        print(capitalize[0].upper(), " ", len(capitalize[0]))

def trial12():
    capitalise = ("hello","my","name","is","Markline")
    case = [i.upper() for i in capitalise]
    length = [len(i) for i in capitalise]
    print(tuple(zip(case, length)))
    
def trial13():
    def factorial(num):
        if num == 1:
            return num
        else:
            return num * factorial(num - 1)


    num = int(input("Enter a Number: "))

    if num < 0:
        print("Factorial cannot be found for negative numbers")
    elif num == 0:
        print("Factorial of 0 is 1")
    else:
        print("Factorial of", num, "is: ", factorial(num))
