#315533067
#Dor Natan

#function 1#
#
# def handle_file(filename="q1.txt", input=''):
#     try:
#         final = ''
#         with open(filename, 'r') as f:
#             my_dict = {}
#             final = f.read().replace(",", " ").replace(".", " ").replace(";", " ")
#             arr = final.split(" ")
#             for i in arr:
#                 if i == '':
#                     arr.pop()
#                 else:
#                     if i in my_dict:
#                         my_dict[i] += 1
#                     else:
#                         my_dict[i] = 1
#             f.close()
#         with open(filename, 'w') as f:
#             f.write(final)
#             f.close()
#         return my_dict
#     except:
#         try:
#             with open(filename, 'w') as f:
#                 f.write(input)
#                 f.close()
#                 raise FileNotFoundError
#         except:
#             return ('File does not exist. Generated file %s' % filename)
#
#
#
# print("Return value with no parameters:\t ", handle_file())
#
# fileInput = "one, two, three, one;two;three; one.two.three many one;one,one;one and one more two"
# myFileName = "myFile.txt"
# handle_file(filename=myFileName, input=fileInput)
# output = handle_file(filename=myFileName)
# print("The result dictionary of the generated file ",myFileName, " is:\t", output)
# handle_file(input=fileInput)
# output = handle_file()
# print("The result dictionary of the generated file q1.txt is:\t", output)

################################################################################################
#
#function 2#
##
# def check_date(date):
#     dt = date.replace(".", " ").replace("/", " ").split(" ")
#     index = 0
#     for d in dt:
#         int(d)
#         index += 1
#     if index != 3:
#         raise Exception("ValueError")
#     if 2021 >= int(dt[2]) >= 1:              # Check if year is ok
#         if 12 >= int(dt[1]) >= 1:                       # Check if month is ok
#             if int(dt[1]) == 2:
#                 if int(dt[2]) % 4 == 0 and int(dt[2]) % 100 != 0 or int(dt[2]) % 400 == 0:        # Check leap year
#                     if 29 >= int(dt[0]) >= 1:
#                         return True
#                     else:
#                         raise Exception("day out of range")
#                 else:
#                     if 28 >= int(dt[0]) >= 1 :
#                         return True
#                     else:
#                         raise Exception("day out of range")
#             elif int(dt[1]) in [4, 6, 9, 11]:
#                 if 30 >= int(dt[0]) >= 1:
#                     return True
#                 else:
#                     raise Exception("day out of range")
#             elif int(dt[1]) in [1, 3, 5, 7, 8, 10, 12]:
#                 if 31 >= int(dt[0]) >= 1:
#                     return True
#                 else:
#                     raise Exception("day out of range")
#         else:
#             raise Exception("month out of range")
#     else:
#         raise Exception("year out of range")
#
#
# dateStr = '29/2/60'
# print(dateStr, ' date is valid? ', check_date(dateStr))
# dateStr = '29/03/2020'
# print(dateStr, ' date is valid? ', check_date(dateStr))
# try:
#     dateStr = "35/05/2020"
#     check_date(dateStr)
# except Exception as e:
#     print("Exception for date:\t", dateStr, e)
# try:
#     dateStr = "29/02/2021"
#     check_date(dateStr)
# except Exception as e:
#     print("Exception for date:\t", dateStr, e)
# try:
#     dateStr = "1/22/2020"
#     check_date(dateStr)
# except Exception as e:
#     print("Exception for date:\t", dateStr, e)
# try:
#     dateStr = "a/11/2020"
#     check_date(dateStr)
# except Exception as e:
#     print("Exception for date:\t", dateStr, e)

#
######################################################################################
#
#function3#

# def four_fibA(n):
#     if n<4:
#         return n
#     four_fib = four_fibA(n-1) + four_fibA(n-2) +four_fibA(n-3) +four_fibA(n-4)
#     return four_fib
#
# print(four_fibA(5))
# print(four_fibA(10))


# fibB_lookup = {0:0,1:1,2:2,3:3}
# def four_fibB(n):
#     if n in fibB_lookup.keys():
#         return fibB_lookup[n]
#     fibB_n = four_fibB(n-1) + four_fibB(n-2) +four_fibB(n-3) +four_fibB(n-4)
#     fibB_lookup[n] = fibB_n
#     return fibB_n
#
# print(four_fibB(10))
# print(four_fibB(100))

####################################################################################################
#
#function 4 #
#
# climb_lookup = {1:1, 2:2}
# def climb_combinations(n):
#     if n in climb_lookup.keys():
#         return climb_lookup[n]
#     climb_n = climb_combinations(n-1) + climb_combinations(n-2)
#     climb_lookup[n] = climb_n
#     return climb_n
#
# for i in range(1,20):
#     print(climb_combinations(i),end= " ")
