# lst = [1, 10 ,7 ,6, 2, 11]

# # print(sorted(ls, reverse=True))

# def max min(ls):

#     # max = 0
#     # for range(0,len(ls))

#     for val in ls:
#         if 

#         max<-0
#     return max
#--------------------------------

# max=ls[0]
# min=ls[0]
# for i in range(l, len(ls)):
#       if ----- :
#          -----
#       if ----- :
#          -----   
#           -1<0
#       return [max,min]
#       

#--------------------------------


# def key_func(n):
#     return str(n)
# ls = [1, 10 ,7, 6, 2, 11]
 
# print(max(ls, key=key_func), min(ls, key=key_func))

#------------------------------------------------------

# lst=[1,10,7,6,2,11,-1]
# def max_min(ls):
#     max = ls[0]
#     min = ls[0]
#     for i in range(1, len(ls)):
#         if max < ls[i]:
#             max=ls[i]
            
#         if min > ls[i]:
#             min=ls[i]
            
#     return[max,min];

# print('max,min:',max(lst), min(lst))

#2番
list=[10,50,60,100,0]
def max_min(list):
    max=list[0]
    min=list[0]
    for i in list:
        if i > max:
            max = i

        elif i< min:
            min = i

    return (max,min)
    return(max_min)

print(max_min(list))