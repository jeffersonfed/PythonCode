# mylist = [10, 70, 100, 60, 20, 90, 80]
# ave = sum(mylist) / len(mylist)
# print(ave)
#--------------------------------------------

# ave1 = [10, 70, 100, 60, 20, 90, 80];
# def ave(num):
#     wa = 0
#     for val in num:
#         wa = wa + val           

#     avg = wa / len(num)
#     return avg

# print("average is", ave(ave1))

from rnd_lib import *

list=[10,5.5,60,100,0]
def avg(list):
    wa=0
    for i in range(1,len(list)):
        wa+=list[i]

    ag=wa/len(list)
    return ag

av=avg(list)

print(av)
print(rnd(av,2))





# def ave(num):
#     sum = 0
#     for val in num:
#         sum = sum + val           

#     avg = sum / len(num)
#     return avg

# print("average is", ave([10, 70, 100, 60, 20, 90, 80]))