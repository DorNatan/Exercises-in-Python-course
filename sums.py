# Dor Natan
# 315533067
int_list = [int(x) for x in input("please enter the numbers,separated by space: ").split()]
for i in range(len(int_list)):
    for j in range(len(int_list)):
        for k in range(j+1,len(int_list)):
            if int_list[j] + int_list[k] == int_list[i]:
                print(int_list[j],"+",int_list[k],"=",int_list[i])

