"""
message = "Hello Python world!"
print(message) 
message = "Hello Python Crash Course world!" 
print(message) 
message = 'i told my friend, "Python is my favorite language!"'
print(message.title()) 
message = "The language 'Python' is named after Monty Python, not the snake."
print(message.upper());
message = "One of Python's strengths is its diverse and supportive community."
print(message.lower())
#用拼接
print(message.lower()+'hhh')
#使用制表符或换行符来添加空,添加制表符，可使用字符组合\
fff="\tPython";
#lstrip rstrip strip删除空白格
print(fff.lstrip());
#添加换行符，可使用字符组合\n
print("Languages:\nPython\nC\nJavaScript")
age = 23;
message = "Happy " + str(age) + "rd Birthday!" 
print(str(message))
bicycles = ['trek', 'cannondale', 'redline', 'specialized']; 
print(bicycles);print(bicycles[0])
print(bicycles[0].title())
#通过将索引指定为-1 ，可让Python返回最后一个列表元素
print(bicycles[-1])
#motorcycles.append('ducati')
bicycles.append('ducati')
bicycles.insert(0, 'ducati111')
del bicycles[0]
print(bicycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles) 
popped_motorcycle = motorcycles.pop()
print(motorcycles) 
print(popped_motorcycle)
"""
# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles1 = ['honda1', 'yamaha1', 'suzuki1']
# print(motorcycles+motorcycles1)
# if True:
#     print ("Answer")
#     print ("True")
# else:
#     print ("Answer")
#     print ("False")

# str = 'Runoob'

# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始后的所有字符
# print(str * 2)  # 输出字符串两次
# print(str + '你好')  # 连接字符串

# dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
#
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ", dict['Age'])


# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2) * 5
#     print("对应人类年龄: ", human)
# input("点击 enter 键退出")

# 该实例演示了数字猜谜游戏
# number = 7
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")

# n = 100
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
# print("1 到 %d 之和为: %d" % (n, sum))
# var = 1
# while var == 1:  # 表达式永远为 true
#     num = int(input("输入一个数字  :"))
#     print("你输入的数字是: ", num)
#
# print("Good bye!")
# for i in range(5):
#     print(i)
# for i in range(5, 9):
#     print(i)
#
# for i in range(0, 10, 3):
#     print(i)
#
# for i in range(-10, -100, -30) :
#     print(i)
#
# a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
# for i in range(len(a)):
#     print(i, a[i])


# for letter in 'Runoob':  # 第一个实例
#     if letter == 'o':  # 字母为 o 时跳过输出
#         continue
#     print('当前字母 :', letter)
#
# var = 10  # 第二个实例
# while var > 0:
#     var = var - 1
#     if var == 5:  # 变量为 5 时跳过输出
#         continue
#     print('当前变量值 :', var)
# print("Good bye!")

# list=[1,2,3,4]
# it = iter(list)
# print(it)
# print(next(it))

# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         x = self.a
#         self.a += 1
#         return x
# myclass = MyNumbers()
# myiter = iter(myclass)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
#
# import sys
#
#
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
#
#
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
#

# 计算面积函数
# def area(width, height):
# #     return width * height
# # def print_welcome(name):
# #     print("Welcome", name)
# # print_welcome("Runoob")
# # w = 4
# # h = 5
# # print("width =", w, " height =", h, " area =", area(w, h))

# 以下实例我们可以输出函数的注释：

def a():
    '''这是文档字符串__doc__'''
    pass
print(a.__doc__)

# import _thread
# import time
#
# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: 无法启动线程")
#
# while 1:
#    pass