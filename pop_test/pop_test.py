# import time


# a= [1,2,3,4,3,3,4,5,2,2,22,534]
# 单数= []
# 双数= []

# for i in a :
#     if i%2==0:
#         双数.append(i)
#         print(f'现在的双数有{len(双数)} 个。')
#         time.sleep(1)
#     else:
#         单数.append(i)
#         print(f'现在的单数有{len(单数)} 个。') 
#         time.sleep(1)


# for i in range(10):
#     print(i)
lst= list(range(1,10))
lst2= 1

while lst2 < 10:
    for i in lst:
        print(f'{lst2}乘{i}得：',i*lst2)
        

    lst2+=1

# print(len(lst))