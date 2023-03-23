# def call(cp):
#     def add50():
#         result= 0
#         for i in range(51):
            
#             result+= i
#         # print(result)
#         cp(result)
#     return add50

# @call
# def pd(a):
#     print('nomal code',a)

# pd()


def factory_doc(n,m,b):
    def cp(ap):
        def sumall():
            num= 0
            num= n+m+b

            ap(num)
        return sumall
    return cp
num1= int(input('请输入第一个数：'))
num2= int(input('请输入第二个数：'))
num3= int(input('请输入第三个数：'))
@factory_doc(num1,num2,num3)
def decfunc(a):
    print('nomal code',a)

decfunc()
    


