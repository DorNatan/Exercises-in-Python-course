#Dor Natan
#315533067

from csv import reader

with open('AppleStore.csv', encoding='utf8') as opened_file:
    read_file = reader(opened_file)
    apps_data = list(read_file)


def extract(col):         #פונקציה שמקבלת מספר עמודה ומחזירה רשימה של כל הערכים באותה עמודה
    list = []
    for row in apps_data:
        x = row[col]
        list.append(x)
    return list


numberofcol = int(input("insert a number of col,please: "))
genres = extract(numberofcol)
print(genres)


def freq_table(genres):         # פונקציה שיוצרת טבלת תדירויות בצורת מילון לכל רשימה שתקבל
    dict = {}
    for i in genres:
        count = dict.get(i, 0)
        count = count + 1
        dict[i] = count
    return dict


freq = freq_table(genres)
print('frequency table : ', '\n', freq)


def freq_table_gen(colIndex):                      #פונקציה שמשתמשת בשתי הפונקציות הקודמות כדי ליצור טבלת תדירויות ובנוסף מחזירה את הערך הכי גבוה מתוך המילון
    mylist = extract(colIndex)
    frequency = freq_table(mylist)
    mostPopular = max(frequency, key=frequency.get)
    return frequency, mostPopular


index = int(input("insert a col index, please: "))
Freqtable, mostPopular = freq_table_gen(index)
print('The table frequency is: ', Freqtable, "\n", "The most popular value is: ", mostPopular)
