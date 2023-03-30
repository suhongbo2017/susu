import random
import string

数字= string.digits
字母= string.ascii_letters

密码= list(数字 + 字母)
# print(密码)
random.shuffle(密码)

print(密码[:6])

