##Dor Natan
##315533067

import math
value = (input('Please enter the area you want to calculate R or r for rectangle, C or c for circle: '))
if value == 'R':
    width_height = (input('Please enter width and height of the rectangle separated by comma: '))
    answer = (width_height.split(','))
    width = (float(answer[0]))
    height = (float(answer[1]))
    area_rectangle = width*height
    print('The area of a rectangle with width', width, 'and height',height,'is:',area_rectangle)
elif value == 'r':
    width_height = (input('Please enter width and height of the rectangle separated by comma: '))
    answer = (width_height.split(','))
    width = (float(answer[0]))
    height = (float(answer[1]))
    area_rectangle = width*height
    print('The area of a rectangle with width', width, 'and height',height,'is:',area_rectangle)
elif value == 'c':
    radius = float(input('please enter the radius: '))
    area_circle = radius**2 * math.pi 
    print('The area of a circle with radius',radius,'is:',area_circle)
elif value == 'C':
    radius = float(input('please enter the radius: '))
    area_circle = radius **2 * math.pi 
    print('The area of a circle with radius',radius,'is:',area_circle)
else:
    print('option', value,'does not exist')
