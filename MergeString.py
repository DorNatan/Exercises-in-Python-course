s1= input('enter a first string ,please: ')
s2= input('enter a second string ,please: ')
if len(s1)%2 == 0:
    mid = len(s1) // 2 
    s1new = s1[0:mid]
    s1new2 = s1[mid:]
    s1new = s1new + s2 + s1new2
    print (s1new)
else:
    mid = len(s1) // 2
    s1new = s1[:mid]
    s1new2 = s1[mid:]
    s1new = s1new + s2 + s1new2
    print (s1new)
    
    
