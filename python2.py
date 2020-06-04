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
#
# 函数参数
#
#
# 默认参数
# def power(x, n=2):
#     s = 1
#     while n > 0:
#         n = n-1
#         s = s*x
#     return s
#
#
# print(power(5, 3))
#
# 注意： 1. 必选参数在前，默认参数在后，否则Python解释器会报错。
#       2. 如何设置默认参数。当函数有多个参数时，把变化大的参数放在前面，变化小的参数放后面,
# 变化小的参数就可以作为默认参数。
# 使用默认参数可以降低函数的调用难度。
#
# 默认参数也是一个变量，如果是引用变量，重复调用时默认参数就改变了，会出现问题：
# def add_end(L=[]):
#     L.append("end")
#     return L
#
#
# print(add_end())-------------->['end']
# print(add_end())---------------->['end', 'end']
# 所以默认参数必须指向不变对象。
#
#
# 为什么要有不变的对象，如str None :
# 1.不变的对象一旦创建，对象内部数据就不能修改，这样就减少了由于数据修改而导致的错误。
# 2.由于对象不变，多任务环境下同时读取对象时不需要加锁。
#
#
# 可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n*n
#     return sum
#
#
# print(calc(1, 2, 3))
# print(calc(1, 2))
# print(calc())
# 定义可变长参数时，只需要在参数前面加一个*号，在函数内部，参数收到的是一个tuple，因此函数代码完全不变。
# 在调用参数时可以传入任意个参数，包括0个参数。
#
#
# 如果现在已经有一个list或tuple 但是函数参数是可变长参数怎么办，解决方法有两种：
#   1.将list或tuple拆开传到函数里，calc(num[0], num[1], num[2])
#   2.Python允许在list或tuple 前面加一个*号，把list或tuple的元素变成可变长参数传进去：calc(*num),num=[1,2,3]
# 其中，*num 代表把num这个list的所有元素作为可变长参数传进去。
#
# ! 感叹号表示Alert
# ? 问号表示Queries
# TODOs:TODOs表示待办事项
# * 表示高亮
#
#
# !关键字参数，关键字参数可以扩展函数功能
# 关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数内部自动组装为一个dict
# def person(name, age, **kw):
#     print('name', name, 'age', age, 'other', kw)
#
#
# person('Michael', 30)
# person('Bob', 35, city='Beijing')
# person('Adam', 45, gender='M', job='Engineer')
# * 下面**extra表示把extra这个dict的所有key-value用关键字参数传入到函数**kw参数，
# * kw将获得一个dict，注意在kw这个dict只是extra的一个拷贝，对kw的改动不会影响到函数外的extra
# extra={"set": 'qwer'}
#  person('Yancey', 32, **extra)
#
#
#
#
#
# ! 命名关键字参数。
# 对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。至于传的哪些参数，需要在函数内部通过kw检查，如：
# def person(name, age, **kw):
#     if 'city' in kw:
#         # 有city参数
#         pass
#     if 'job' in kw:
#         # 有job参数
#         pass
#     print('name', name, 'age', age, kw)
#
#
# person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)
# !为了限制关键字的名字,可以用命名关键字参数，如只接收city和job作为关键字参数，这种方式定义如下：
# ! def person(name, age, *,city , job):
# !     print(name, age, city, job)
# ! 和关键字参数**kw不同,命名关键字参数需要需要一个特殊分隔符 * , * 后面的参数被视为命名关键字参数。
# ! 其调用方式如下：
# ! person('Jack', 24, city='Beijing', job='Engineer')
#
#
# !如果函数定义中已经有了一个可变参数,后面跟着命名关键字参数就不再需要一个特殊的分隔符*了。
# def person(name, age, *args, city, job):
#     print(name, age, args, city, job)
#
#
# person('张三', 23, 123, 234, city='Beijing', job='hardware')
#
# 当命名关键字有默认值时，可以不传入该参数。
# 命名关键字参数必须传入参数名，和位置参数不同，如果不传入参数名会报错。
# ! 使用命名关键字时，特别注意，如果没有可变长参数，就必须加一个*作为分隔符,缺少*，Python解释器将无法识别位置参数和命名关键字参数
#
#
#
#
# ! 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这五种参数都可以组合使用。
# ! 但是参数的定义顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b = ', b, 'c = ', c, 'args = ', args, 'kw = ', kw)
#
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a = ', a, 'b = ', b, 'c = ', c, 'd = ', d, 'kw = ', kw)
#
#
# f1(1, 2)
# !还可以通过一个tuple和dict，调用上述函数：
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
# !所以对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论他的参数是如何定义的。
# !虽然可以组合多大5种参数，但不要同时使用太多的组合，否则函数接口的可理解性很差！
#
#
#
# 递归函数
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n - 1)
# print(fact(1))
# print(fact(5))
# print(fact(100))
# print(fact(1000))  # !堆栈会溢出
# !解决堆栈溢出的方法是通过尾递归优化，事实上尾递归和循环效果是一样的，所以，把循环看成一种特殊的递归也是可以的。
# ! 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
# ! 这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个堆栈，不会出现栈溢出的情况。
# 上面的函数做成尾递归的形式：
#
#
# def fact(n):
#     return fact_iter(n, 1)
#
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
#
# print(fact(100))
# ! 遗憾的是Python标准的解释器并没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。
