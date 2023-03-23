# class student:

#     def __init__(self,name,age,city):
#         self.name= name
#         self.age= age
#         self.city= city
#         # all= name+age+city
    
#     def is_age(self):
#         if self.age >= '24':
#             return True
#         else:
#             return False
        
#     def add(self,num1,num2):
#         num= num1+num2
#         return num        
# student1= student('苏洪波','21','HuNan_LouDi_LengShuiJiang')
# print(student1.is_age())
# print(student1.add(34,66))


class phone:
    def __init__(self,number,year,is_waterporf):
        self.number= number
        self.year= year
        self.is_waterporf= is_waterporf

phone1= phone(122,'2023','Ture')
phone2= phone(123,'2023','False')
phone3= phone(124,'2023','Ture')
print(phone1.year)