import math
while True:
    def addition (a,b):
        return a+b
    def subtraction (a,b):
        return a-b
    def multiplicatiom (a,b):
        return a*b
    def division (a,b):
        return a//b
    def power (a,b):
        return a**b
    def log (c,d):
        return math.log(d,c)

    a= int(input('enter the first value a--->'))
    b= int(input('enter the second value b--->'))
    c= int(input('enter the log base value---->'))
    d= int(input('enter the value which log should be calculated--->'))
    print('enter the operation operator you want to exercise, +,-.*,//, **,log')
    

    operator= input()
    if operator == '+':
        print (a+b)
    elif operator == '-':
        print (a-b)
    elif operator == '*':
        print (a*b)
    elif operator == '//':
        print (a//b)
    elif operator=='**':
        print (a**b)
    elif operator == 'log':
      print ("log base c of d is : ",math.log(d,c))
    else:
        print ('\n\t Invalid operator!')
                 
