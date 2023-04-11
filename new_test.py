
# 函数
def 加法(x,y):
    return x+y
def 减法(x,y):
    return x-y
def 乘法(x,y):
    return x*y
def 除法(x,y):
    商= x//y
    余= x%y
    return 商,余


while True:
    计算类型= input('请选择计算类型(1,加法 2,减法 3,乘法 4,除法):')
    if 计算类型 in ('1','2','3','4'):
        数字1= int(input('请输入第一个数字:'))
        数字2= int(input('请输入第二个数字:'))
        if 计算类型 == '1':
            print(f'{数字1}加{数字2}等于{加法(数字1,数字2)}')

        elif 计算类型 == '2':
            print(f'{数字1}减{数字2}等于{减法(数字1,数字2)}')

        elif 计算类型 == '3':
            print(f'{数字1}乘{数字2}等于{乘法(数字1,数字2)}')

        elif 计算类型 == '4':
            if 数字1 % 数字2 == 0:

                print(f'{数字1}除{数字2}等于{除法(数字1,数字2)[0]}')

            else:

                print(f'{数字1}除{数字2}等于{除法(数字1,数字2)[0]}余{除法(数字1,数字2)[1]}')

    else:
        continue




# 装饰器
# def abbb(callback):
#     def sumny():
#         c= a*b
#         callback
#     return sumny()
# a= input('请输入：')
# b= input('请输入：')
# c= 0
# @abbb
# sumny(a,b)


# 装饰器工厂
 