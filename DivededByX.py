# Dor Natan
# 315533067
div = []
div2d = []
x = int(input("please enter a number: "))
for row in range(10):
    for col in range(10):
        num = int(col + row * 10 + 1)
        if num % x == 0:
            div.append(num)
    div2d.append(div.copy())
    div.clear()
print(div2d)



