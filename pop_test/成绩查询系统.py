
grading_system= {'小红':67,'火鸡':88,'田田':78,'阿B':98}

print('欢迎进入成绩查询系统：（A,查询成绩、B，删除成绩、C，增加成绩、D，修改成绩。）')
command= input('请输入：').upper()

print(command)
while not (command == 'A' or command == 'B' or command =='C' or command == 'D'):
    print('（A,查询成绩、B，删除成绩、C，增加成绩、D，修改成绩。）')
    command= input('请输入：').upper()

if command == 'A':
    name= input('请输入学生姓名：')
    # print(name)
    while not (name in grading_system):
        print('查无此人，请重新输入：')
        name= input('请输入学生姓名：')
    
    print(f'{name}的成绩是{grading_system[name]}分。')

elif command == 'B':
    name= input('请输入要删除的学生姓名：')
    
    while not (name in grading_system):
        print('查无此人，请重新输入：')
        name= input('请输入学生姓名：')
    del_name= input('你确认要删除吗？（Y）').upper()
    print('确认删除请输入“Y”，返回按其它键：')

    while not (del_name == 'Y'):
        name= input('请输入要删除的学生姓名：')
    grading_system.pop(name)
    print(f'学生"{name}"已经被删除。')
    print(grading_system)
    

elif command == 'C':
    add_name= input('请输入要新增学生姓名：')
    sure_name= input(f'确认新增{add_name}吗？（Y）').upper()
    while not (sure_name == 'Y'):
        add_name= input('请输入要新增学生姓名：')
    add_grading= input('请输入要新增的成绩')
    sure_grading= input(f'确认新增{add_grading}吗？（Y）')
    while not (sure_grading == 'Y'):
        add_name= input('请输入要新增学生姓名：')
    grading_system[add_name]= int(add_grading)
    print(f'新增学生“{add_name}”的成绩“{add_grading}”完成。')




else:
    print('')