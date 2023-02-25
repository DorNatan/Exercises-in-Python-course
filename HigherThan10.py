# Dor Natan
# 315533067
higherThen10 = []
exit_Value = -1
minvalue = 10
flag = False
while not flag:
    num = int(input("insert a number please: "))
    if num == exit_Value:
        flag = True
    elif num > minvalue:
        higherThen10.append(num)

print("The numbers are: ")
for i in range (len(higherThen10)):
    print(higherThen10[i])
