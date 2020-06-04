# -*- coding:utf-8 -*-
# 函数
# python 有很多内置函数 官方文档http://docs.python.org/3/library/functions.html
# help(abs) 查看abs函数的信息
# abs(1,2) 在调用函数时，如果参数数量不正确，会报TypeError错误,比如abs()需要一个参数，但传递参数时传了两个参数，Python会报一个TypeError的错误，
# 并且会明确的告诉你：abs()只有一个参数，但是你传了两个。
# abs('a') 如果传入的参数数量是对的,但是参数类型不能被函数所接受，也会报TypeError的错误，并且给出错误信息：str是错误的参数类型。
# max()函数可以接受任意数量的参数，并返回最大的那个。
#
# 数据类型转换函数
# int()   将其他类型的参数转换为int类型，str必须是整数格式不能带小数点，而浮点数只保留整数部分。
# float() 将其他类型转换为float类型。
# str() 将其他类型转换成str类型。
# bool() 将输入的值转换为布尔类型的值，被定义为假值的常量：None，False;任何数值类型的零：0，0.0，0j,Decimal(0),Fraction(1,0);空的序列和多项集：'',(),[],{},set(),range(0)
#
# 函数其实是一个指向函数对象的引用，可以把函数名赋给另一个变量,相当于给函数起了一个别名:
# a = abs # 变量a指向abs函数。
# a(-1) #所以也可以通过a调用abs函数。
# hex() 十六进制转换函数。
# 31dce6513e467a769bab0e1d06149f9f
#
# 定义函数
# 定义函数要使用 def关键字，后面依次为函数名、括号、括号中的参数和冒号，然后在缩进块中编写函数体，函数有返回值的话用return关键字。
# def my_abs(x):
#    if x >= 0:
#        return x
#    else:
#        return -x
#
#
# print(my_abs(-99))
# 函数体内部的语句在执行时，一旦执行到return时，函数就执行完毕，并返回结果。
# 如果没有return语句，函数执行完毕后返回None，return None 可以简写为return 。
#
# 如果你已经把my_abs()的函数定义保存为abstest.py文件,那么可以在该文件的当前目录下启动Python解释器，
# 用from absttest import my_abs 来导入my_abs()函数，注意abstest是文件名(不含.py扩展名。)
# from absttest import my_abs
# print(my_abs(-10))
#
# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句。
# def nop():
#    pass
# pass 可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码运行起来。
# pass还可以用在其他语句里面，比如：
# if age >= 18:
#     pass
# 缺少了pass，代码运行就会有语法错误。
#
#
# 参数检查
# 对参数类型做检查,只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现。
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# print(my_abs(12))
#
#
# 返回多个值
# import math
#
#
# def move(x, y, step, angle=0):
#    nx = x + step * math.cos(angle)
#    ny = y - step * math.sin(angle)
#    return nx, ny
#
#
# x, y = move(100, 100, 60, math.pi / 6)
# print(x, y)----- >151.96152422706632 70.0
# print(move(100, 100, 60, math.pi / 6)) --------------------> (151.96152422706632, 70.0)
#
# 所以Python函数返回的仍然是单一值。多值返回的是一个tuple，在语法上，返回tuple可以省略括号，而多变量可以同时接收一个tuple,
# 按位置赋值给对应的值，所以，Python 的函数返回多值就是返回一个tuple，但是写起来方便。
#
# 作业
# import math
#
#
# def quadratic(a, b, c):
#    if not (isinstance(a, (int, float) or isinstance(b, (int, float) or isinstance(c, (int, float))))):
#        raise TypeError("bad operater type")
#    x1 = (-b+math.sqrt(b*b-4*a*c))/2*a
#    x2 = (-b-math.sqrt(b*b-4*a*c))/2*a
#    return x1, x2
#
#
# print(quadratic(2, 3, 1))
# print(quadratic(1, 3, -4))
#