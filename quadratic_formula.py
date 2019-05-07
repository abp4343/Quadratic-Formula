print('standard form of a quadratic: ax^2 + bx + c = 0')
print('Put your quadratic in standard form.')

a = float(input("What is a? "))
b = float(input("What is b? "))
c = float(input("What is c? "))
option_1 = 0
option_2 = 0

if ((b*b)-(4*a*c)) < 0:
    print('answer involves imaginary numbers')
else:
    option_1 = ((-b + (((b*b)-(4*a*c))**(1/2)))/(2*a))
    option_2 = ((-b - (((b*b)-(4*a*c))**(1/2)))/(2*a))
    print('x = ' + str(option_1) + ' , ' + str(option_2))