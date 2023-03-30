import random
class user():
    life= 1000
    attac= 150
    def __init__(self,name):
        self.name= name
    def hold(self,command):
        if command == 1:

            print('铁壁！')
            return 0.5
        else:
            print('隐形')
            return 0
    
class soldr(user):
    def A(self):
        print('一拳')
        return 1
    def B(self):
        print('一脚')
        return random.choice([1.5,0])
    
class xxx(user):
    lif= 2000
    att= 230
    def A(self):
        print('一爪')
        return 1
    def B(self):
        print('一脚')
        return random.choice([1.5,0])
    
gamer= soldr(user('王大山'))
se= xxx.
while True:
    command= input('请选择hold方式1,2:')
    gamer.life -=gamer.hold(command)
    print(gamer.life)



    