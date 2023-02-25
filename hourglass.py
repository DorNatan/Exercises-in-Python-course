# Dor Natan
# 315533067
n = int(input("Please enter number of rows: "))
spaces = 0
stars = 0
for i in range(n):
    if i >= 0 and i <= (n-1)//2:
        spaces = i
        stars = n-(i*2)
    elif i>n//2: # if (n%2==0) and (i==n//2) do nothing
        spaces -= 1
        stars = stars + 2
    for j in range(spaces):
        print(end=" ")

    for j in range(stars):
        print("*", end="")

    print()
