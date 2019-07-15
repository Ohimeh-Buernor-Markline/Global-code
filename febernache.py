def trial1():    #This function is for the FIBONACCI
    def feb(n):
        if n == 0:
            return n
        elif n == 1:
            return n
        elif n > 1:
            return (feb(n-1)+feb(n-2))
    
    n = int(input("Enter a number: "))
    print("Feb of ", n ," = ",feb(n))
    print(list(range(1,n+1)))
    print(list(map(feb,range(1,n+1))))



def trial2():      #This function is for factorial
    def fact(n):
        if n == 1:
            return 1
        else:
            return n*fact(n-1)
    n = int(input("Enter a number here: "))
    
    print("The factorial of ", n, " = ", fact(n))
    print(list(map(fact,range(1,n+1))))
trial1()    