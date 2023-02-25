##Dor Natan
##315533067

details = (input('Please enter student name included last name and ID separated by space: '))
student_details = details.split(' ')
if len(student_details[2]) != 7:
    print('id must start with 0 and has 7 digits')
elif (student_details[2][0]) != '0':
    print('id must start with 0 and has 7 digits')
elif (student_details[2]).isnumeric():
    print(details)
else:
    print(student_details)
