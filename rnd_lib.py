
#--------------------------
# print (round(su, 2));    |
# def rnd(su,digit):       |
# p = 10 ** n-1;           |
# print (round(su,p));     |
#--------------------------
#1
import math
num = 2.5467
r_val = 2

def rnd(num,r_val):
    multi=10**r_val
    n1=math.floor(num*multi+.5)/multi
    return n1

print(rnd(num,r_val))
     
#---------------------------------
# num1 = 2.55                     |
# print('・Value to round:', num1) |
# num1_ft = format(num1, '.1f')   |
# print('・rnd=:', num1_ft)       |
#---------------------------------
    