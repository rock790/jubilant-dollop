while True:
    def addition (a,b):
        return a+b
    def subtraction (a,b):
        return a-b
    def multiplicatiom (a,b):
        return a*b
    def division (a,b):
        return a//b

    a= int(input('enter the first value a--->'))
    b= int(input('enter the second value b--->'))
    print(' enter the operation operator you want to exercise, +,-.*,//')
    operator= input()
    if operator == '+':
        print (a+b)
    elif operator == '-':
        print (a-b)
    elif operator == '*':
        print (a*b)
    elif operator == '//':
        print (a//b)
    else:
        print ('\n\t Invalid operator!')
                 
