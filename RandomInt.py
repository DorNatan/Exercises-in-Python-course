##Dor Natan
##315533067

##a
import random
rand_num= input('Please enter the range of random numbers from;to: ')
the_num= rand_num.split(';')
n= int(the_num[0])
k= int(the_num[1])
print('The random number between', n, 'and', k, 'is:', random.randint(n,k-1))


##b
lst=[]
ran = (input('Please enter two ranges of random numbers from1;to1 from2;to2: '))
twolst = ran.split(' ')
lst.extend([twolst[0],twolst[1]])
ch = random.choice(lst)
num = (ch.split(';'))
print('The selected range is',num[0], 'to',num[1], 'and the selected number is: ' , random.randint(int(num[0]), int(num[1])))
