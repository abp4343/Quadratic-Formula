print('standard form of a quadratic: ax^2 + bx + c = 0')
print('Put your quadratic in standard form.')

a = float(input("What is a? "))
b = float(input("What is b? "))
c = float(input("What is c? "))
option_1 = 0
option_2 = 0

if ((b*b)-(4*a*c)) < 0:
    real_option_1_2 = -b/(2*a)
    imaginary_option_1_2 = ((abs((b*b)-(4*a*c)))**(1/2))/(2*a)
    print('\n\nimaginary roots found:')
    print('x = ' + str(real_option_1_2) + ' + ' + str(imaginary_option_1_2) + \
    	'i , ' + str(real_option_1_2) + ' - ' + str(imaginary_option_1_2) + 'i')
else:
    option_1 = ((-b + (((b*b)-(4*a*c))**(1/2)))/(2*a))
    option_2 = ((-b - (((b*b)-(4*a*c))**(1/2)))/(2*a))
    print('\n\nreal roots found:')
    print('x = ' + str(option_1) + ' , ' + str(option_2))
