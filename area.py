import math
from math import pi
def shape():
    print('1. Circle')
    print('2. Triangle')
    print('3. Square')
    print('4. Rectangle')
    shape_input = int(input("Please enter the desired shape:- "))
    area(shape_input)
    
    
    # if shape_input == 1:
    #     circle()
    # if shape_input == 2:
    #     triangle()
    # if shape_input == 3:
    #     square()
    # if shape_input == 4:
    #     rectangle()


def area(a):   
    if a == 1:
        c_r = float(input('Enter the radius of circle:- '))
        print ("The area of circle with radius " + str(c_r) + " is: " + str(pi * c_r**2))
    elif a == 2:
        t_l = float(input('Enter the length of triangle:- '))
        t_h = float(input('Enter the height of triangle:- '))
        print ("The area of triangle with length " + str(t_l) + 'and height' + str(t_h) + " is: " + 1/2 * t_l * t_h)
    elif a == 3:
        s_e = float(input('Enter the edge of square:- '))
        print ("The area of square with edge " + str(s_e) + " is: " + s_e**2)
    elif a == 4:
        r_l = float(input('Enter the lenght of rectangle:- '))
        r_b = float(input('Enter the breath of rectangle:- '))
        print('The area of rectangle with length' + str(r_l) + 'and breath' + str(r_b) + 'is:' + r_l * r_b)


shape()