# Dor Natan
# 315533067

def mult_even_digits(n):
    x = 1
    while n > 0:
        rem = n % 10
        if rem % 2 == 0:
            x = x * rem
        n = int(n // 10)
    return x


n = int(input("please enter a intiger: "))
multeven = mult_even_digits(n)
print(multeven)


def fix_grades(gr):
    j = 0
    for i in grades:
        if i <= 50:
            grades[j] = 0
        elif 51 <= i < 60:
            grades[j] = 60
        j += 1
        biggest = 0
        for k in grades:
            if 100 >= k >= 60:
                biggest += 1
    return biggest


grades = [100, 90, 70, 30, 56, 83, 23, 55, 46]
print('Number of passing grades : ', fix_grades(grades), "\n", grades)


def must_popular_digit(intiger):
    dicn = {}
    intiger = str(intiger)
    for keys in intiger:
        dicn[keys] = dicn.get(keys, 0) + 1
    max_val = max(dicn.values())
    max_key = int(max(dicn.keys()))
    for i in reversed(range(10)):
        if i == max_key:
            max_key = str(max_key)
            max_val22 = dicn.get(max_key)
            if max_val == max_val22:
                return max_key
            else:
                max_key = int(max_key)
                max_key -= 1
    return (max_key)


print('must popular digit : ', must_popular_digit(54535354555))
