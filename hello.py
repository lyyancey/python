# -*- coding: utf-8 -*-
# 输入输出:
# name = input('please enter your name:')
# print('Hello ', name)

# 缩进的方式写代码
# a = 100
# if a >= 0:
#    print(a)
# else:
#    print(-a)
# python的数据类型
# 整形：python可以处理任意大小的整数，包括负整数
# 用十六进制表示的方法:0x前缀  0-9 and a-f 表示
# 例如：0xff00 , 0xa5b4c3d2
# print(0xfff00)
# 结果 1048320
# 浮点型：
# 1.23 3.14 -9.01
# 科学计数法1.23e9 1.2e-5等
# 注意：整数与浮点数在计算机内部存储方式是不同的，整数运算永远是精确的（除法难道也是精确的？ 是的！），而浮点数运算则可能会有四舍五入的误差
# 上文中的精确，个人觉得是存储表示的精确，而不是计算结果的精确
#
# 字符串
# 可以用单引号也可以用双引号如 "xyz" 或'xyza'
# print("Hello,I'm Liuyong")
# print('这是"美好"的一天！')
# print('I\'m "Ok"')
# print('I\'m \"Ok\"')
# 转义字符:常见的有\n \t \\等
# print("你好呀\n")
# print("\tHello World \\")
#
# 多行打印
# print('''line1
# line2
# line3''')
# 多行字符串'''....''''前面还可以加上r使用
# print(r'''Hello
# World
# !''')
# 像下面这种空注释，后面不需要跟一个空格
#
# 布尔值 布尔值和布尔代数表示完全一致，一个布尔值只有True、False两种值，要么是True，要么是False，首字母都要大写
# 布尔值可以用 and(与运算) or(或运算) not(非运算)运算
# 3>2 True
# 3>5 False
# True and True ------> True
# True and False -----> False
# False and False -------> False
# 3>2 and 1>3 -------->False
# True or False  ------->True
# 3>2 or 1>3 ---------->True
# not True ------->False
# not False ------->True
# not 1>2------->True
# 布尔类型的变量经常出现在判断条件中
# age = 12
# if age > 18:
#     print("adult")
# else:
#     print("teenager")
#
# 空值 空值在python里是一个特殊的值，用None表示,None不能理解为0，因为0是有意义的，而None是一个特殊的空值
# x = None
# if x is None:
#     print("x 是一个空值")
# else:
#     print("x 不是一个空值")
# type(None)
# None 与其他的空值不一样
# None == 0 ------>False
# None == False  ----->False
# None == "" ------->False
# None == {} -------->False
#
# 变量 变量名的命名规则：变量名必须是大小写英文、数字和下划线的组合，且不能以数字开头。
# python 中赋值号为 = 例如 Answer = True
# python是动态语言（解释型语言），变量在执行的时候才确定变量类型和值，相对的是静态语言(编译型语言)，在执行之前必须确定好类型和值。
# 当执行语句 a='abc'时，Python解释器干了两件事:
#       1.创建一个字符串'abc'
#       2.在内存中创建一个名为a的变量,并把它指向'abc'。
# 当把一个变量a赋值给另一个变量b时，这个操作实际上是把变量b指向变量a所指向的数据。
#
# 常量
# 常量就是不能变的变量，在Python中，通常用全部大写的变量名表示常量，例如：
# PI=3.14159265359
# 但事实上PI仍然是一个变量，Python中没有任何机制保证常量不会改变，所以全部大写的变量名表示常量只是一个习惯上的用法。
#
# 在python中有两种除法，一种是 / 如：
# 10 / 3 ---------->3.3333333333333335
# / 除法计算的结果是浮点数，即使是两个整数恰好整除，其结果也是浮点数，如：
# 9 / 3 --------> 3.0
#  还有一种除法是 // ，称为地板除，两个整数的除法仍然是整数
# 10 // 3 --------->3
# 10.0 // 3.0-------->3.0
# 地板除取的是两者相除的整数部分
# 若想取相除的榆树可进行取余操作
# 10 % 3 --------->1
#
# 对基础类型的变量的赋值是直接修改的变量的值
# x = 1
# y = x
# x = 2
# print(y)
#
# Python 的整数是没有大小限制的，而某些语言的整数根据其存储长度是有限制的，例如Java对32位整数的范围限制在-2147483648 - 2147483647
# Python 的浮点数也没有大小限制，但是超出一定范围就直接表示为inf (无限大)
#
# python的字符串编码问题
# python 使用Unicode编码，所以可以支持中文
# 对于单个字符的编码，Python提供了ord()函数获取字符串的整数表示,chr()函数把编码转换为对应的字符，例如：
# ord('A')------------>65
# ord('中')----------->20013
# ord("中")----------->20013
# chr(65)-------------->'A'
# chr(20013)-------------->'中'
#
# 在知道字符的整数编码的情况下，也可以用十六进制写字符串：
# '\u4e2d\u6587' -------------->'中文'
# Python 的字符串类型是str，在内存中用Unicode表示，一个字符对应若干个字节。如果在网络上传输，或者保存到磁盘上，就需要把str变成以字节为单位的bytes。
# Python 对bytes类型的数据用带b前缀的单引号或双引号表示，如：
# x=b'ABC'
# 区分'ABC'与b'ABC',前者是str，后者是str，后者虽然内容显示的和前者一样，但bytes的每个字符都只占用一个字节
# 用Unicode表示的str通过encode()方法可以编码为指定的bytes,例如：
# 'ABC'.encode('ascii')------------------>b'ABC'
# '中文'.encode('utf-8')--------------->b'\xe4\xb8\xad\xe6\x96\x87'
# 'ABC'.encode('utf-8')-------------->b'ABC'
# 由于中文超出了ascii的编码范围，所以中文不能用ascii编码，会报错：
# '中文'.encode('ascii')------------->UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)
# 在bytes中，无法显示为ASCII编码的范围,用 \x##显示。
#
# 当我们从网络上或磁盘上读取了字节流,那么读到的数据就是bytes。要把bytes变为str，用到的就是decode()方法:
# b'ABC'.decode('ascii')------------'ABC'
# b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')--------------->'中文'
#
# 如果bytes中包含无法解码的字节，decode()方法会报错,例如：
# b'\xe4\xb8\xad\xff'.decode('utf-8')---------------》UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 3: invalid start byte
# 如果bytes中只有一小部分无效的字节，可以传入errors='ignore'忽略错误的字节
# b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')----------->'中'
#
# 要计算str包含多少个字符，可以用len()函数：
# len('ABC')----->3
# len('中文')------->2
# len( b'\xe4\xb8\xad\xe6\x96\x87')-------------->6
# len(b'ABC')---------->3
#
# 由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
# 当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
# #!/usr/bin/env python3
# # -*- coding:utf-8 -*-
# 第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
# 第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
# 申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码：
#
# 格式化
# 在Python中，采用格式化方式和C语言一致，用百分号实现，如：
# 'Hello,%s' %'world'----------->'Hello,world'
# 'Hi, %s,you have $%d' % ('Michael',1000000)-------------->'Hi, Michael,you have $1000000'
#
# 当不确定用什么来格式化字符串时，%s永远起作用，他会把任何数据类型转换为字符串：
# 'Age: %s. Gender:%s' % (25,True)----------->'Age: 25. Gender:True'
#
# 另一种格式化字符串的方法是使用字符串的format()方法,他会用传入的参数一次替换字符串内的占位符{0}、{1}...,这种方式比%要麻烦的多:
# 'Hello,{0},成绩提升了{1:.1f}%'.format('小明',17.125)------------>'Hello,小明,成绩提升了17.1%'
# 当%字符串内的%没有格式化的作用时，这时需要转义，具体做法是：%% ，代表%一个普通字符
# 'growth rate: %d %%' % 7  -------------->'Hello 7 %'
# 'growth rate: %d %%' ------------------->'growth rate: %d %%'
# 'growth rate: %d %' % 7 ---------------->ValueError: incomplete format
#
#
#
# 使用list 和 tuple
#
# list
# python 内置的一种数据类型是列表：list
# list 是一种有序集合，可以随时添加和删除其中元素。
#
# 例如列出班级里所有同学的名字,可以用一个list表示：
classmates = ['Michael', 'Bob', 'Tracy']
classmates[0] = "Hello"
classmates
# print(classmates) -------->['Michael', 'Bob', 'Tracy']
# 上面classmates就是一个list,用len()函数可以获得list元素的个数，如：
# len(classmates)---------------->3
# 用索引来访问list中每一个位置的元素,索引是从0开始的:
# classmates[0]-------->'Michael'
# classmates[1]---------->'Bob'
# classmates[2]-------------->'Tracy'
# 当索引超出了范围时，Python会报一个IndexError的错误，所以，要确保索引不要越界,最后一个元素的索引是len(classmates)-1
# classmates[3]---------------->IndexError: list index out of range
#
# 如果要取最后一个元素，除了计算索引位置外，还可以使用-1做索引
# classmates[-1]------------->'Tracy'
# 以此类推，可以获取倒数第二个，倒数第三个
# classmates[-2]-------------->'Bob'
# classmates[-3]-------------->'Michael'
# 在倒数第四个的时候就越界了
# classmates[-4]------------->IndexError: list index out of range
#
# 往list中追加元素的操作为：
# classmates.append("Adam")
# classmates -------------->['Michael', 'Bob', 'Tracy', 'Adam']
# 把元素插入到指定位置，如：
# classmates.insert(1,"Jack")
# classmates--------------->['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
#
# 要删除list 末尾的元素，用pop()方法：
# classmates.pop()----------------->'Adam'
# classmates-------------------->['Michael', 'Jack', 'Bob', 'Tracy']
#
# 要删除指定位置的元素,用pop(i)方法，其中i是索引位置
# classmates.pop(1)-------------->'Jack'
#
# 要把某个元素替换成别的元素，可以直接复制给对应的索引位置
# classmates[1] = 'Sarah'
# classmates-------------------->['Michael', 'Sarah', 'Tracy']
#
# list 里面的元素的数据类型可以不同，如：
# L = ["Apple",123,True]
# L------------------>['Apple', 123, True]
#
# list 元素也可以是另一个list,例如：
# s = ['python', 'java', ['asp', 'jsp'], 'scheme']
# s----------------->['python', 'java', ['asp', 'jsp'], 'scheme']
# 上面的s中只有四个元素，可以把['asp', 'jsp']理解为一个引用变量
# 要拿到s中的jsp,可以用s[2][1]
# s[2][1]--------------->'jsp'
#
# 或者
# s1 = ['asp', 'jsp']
# s2 = ['python', 'java', s1,'php']
# s1[1]------------------>'jsp'
#
# 可以把s看作是一个二维数组，类似的还有三维、四维等等
#
# 如果list中一个元素也没有，就是一个空list，它的长度是0：
# l=[]
# len(l)----------------------->0
#
# tuple(元祖)
# 另一种有序表叫做元祖
# tuple与list非常类似,但是tuple一经初始化就不能修改，如：
classmates = ('Michael', 'Bob', 'Tracy')
# 一旦定义了tuple，他的值就不能改变了,他没有append(),insert()这样的方法,其他获取值的方法与list一样，比如classmates[0]
# classmates[-1],但是不能赋值成另外的元素了。
# 因为tuple不可变，所以代码就更安全，所以如果可以的话，尽量用tuple代替list
# 注意：当定义一个tuple，tuple的元素就必须确定下来
# 如果定义一个空tuple时，可以写成()
#
# 当定义只有一个元素的tuple时，如果写成t=(1),这样定义的不是tuple而是数字1，这种情况下(),代表的是数学公式中的小括号
# 所以当tuple只有一个元素时，在该元素后面加一个逗号，用来消除歧义，如：t = (1,)
# 当python显示只有一个元素的tuple时，也会在该元素后面加一个逗号，以免引起误会，如：(1,)
#
# tuple中有两种元素，一种是基本类型，在tuple中存的是值，还有一种是引用类型，比如说一个list
# 当tuple存储的是引用类型的变量时，引用本身不可以变，但是引用指向的值是可以变的，如：
# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'Y'
# t[2][1] = 'X'
# t---------------->('a', 'b', ['Y', 'X'])
#
#
# 条件判断
# 以下情况只要x是非零数值、非空字符串、非空list、非空tuple就判断为True,都则就判断为False
# x = []
# if x:
#    print(True)
# else:
#    print(False)
#
#
# 再议input(),input()函数返回的是str,如果想把它转换为int,可以用int()函数，如：
# s = input("birth:")
# birth = int(s)
# if birth > 2000:
#     print("00后")
# elif birth > 1990:
#     print("90后")
# else:
#     print("老人！")
#
#
# 循环
# for循环
# 例1
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#    print(name)
#
# 例2
# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum+x
# print(sum)
#
# 例3
# range(x) 可以生成0 - x-1 的一个整数序列，在通过list()函数可以转换为list：
# list(range(5)) -------> [0, 1, 2, 3, 4]
#
# sum = 0
# for x in list(range(101)):
#     sum = sum+x
# print(sum)
#
# while 循环
# 例 1
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n-2
# print(sum)
# 例 2
# L = ['Bart', 'Lisa', 'Adam']
# for x in L:
#    print(x)
#
# break break 可以提前跳出循环
# 例 1
# n = 1
# while n <= 100:
#     if n > 10:
#         break
#     print(n)
#     n = n+1
# print('END')
#
#
# continue 作用：提前结束本轮循环，并直接开始下一轮循环
# 例 1
# n = 0
# while n < 10:
#     n = n+1
#     if n % 2 == 0:
#         continue
#     print(n)
#
#
# dict 和 set
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Michael']
#
# 通过key 向 dict中放入key - value
# d['Adam'] = 67
# d {'Michael': 95, 'Bob': 75, 'Tracy': 85, 'Adam': 67}
# 由于一个key只能对应一个value， 所以，多次对同一个key放入value，后放的value会把前面放的value冲掉。
# d['Bob']-------->75
# d['Bob'] = 86
# d['Bob']----------------->86
#
# key不存在dict就会报错
# d['Thomas']------------>KeyError: 'Thomas'
# 为了避免key不存在的错误,有两种办法：
#  一是通过 in 判断 key 是否存在
# 'Thomas' in d ------------->False
#  二是通过dict提供的get()方法,如果key不存在，可以返回None，或者自己制定的value
# d.get('Thomas') ---------->None 返回None的时候,Python的交互环境不显示结果
# d.get('Thomas', -1)
#
# 要删除 key,用pop(key)方法,对应的 value 也会从dict中删除
# d.pop('Bob')
# d----------------> {'Michael': 95, 'Tracy': 85}
#
# 注意：dict 内部存放的顺序和key放入的顺序是没有关系的。
# 和 list 比较，dict有以下几个特点：
#    1.查找和插入的速度极快，不会随着 key 的增加而增加。
#   2.需要占用大量的内存，内存浪费严重。
# 而 list 则相反：
#   1.查找和插入的时间随着元素的增加而增加;
#   2.占用空间少，浪费内存很少.
# 综上所述，dict是用空间换时间的一种方式。
# dict 可以用在需要需要高速查找的很多地方，在Python代码中几乎无处不在，
# 正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
# 采用的原理是Hash 算法
# 保证Hash值的不可变性，key值就不能变，
# 字符串，整数，等都是不可变的，因此可以放心的作为key
# 而list是可变的就不能作为key
# k = [1, 2, 3]
# d[k] = 'a list' ---------------->TypeError: unhashable type: 'list'
#
#
#
# set
# set 与 dict 类似，也是一组 key 的集合，但不会存储 value ,由于 key 不能重复 ，所以 set 中没有重复的 key 。
# 要创建一个 set ,需要提供一个 list作为输入集合，如：
# s = set([1, 2, 3])
# s------->{1, 2, 3}
# 以上代码中，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1,2,3这三个元素,显示即使是有序的，也不表示set是有序的。
#
# set中，重复的元素会被自动过滤：
# s = set([1, 2, 2, 3, 3])
# s --------------->{1, 2, 3}
#
# 通过add(key)方法可以添加元素到set中,可以重复添加但是不会有效果
s = set([1, 2, 3, 4])
# s.add(5)
# s----------------->{1, 2, 3, 4, 5}
# s.add(5)
# s---------------->{1, 2, 3, 4, 5}
# 通过remove(key)方法可以删除元素
# s.remove(5)
# s-------------->{1, 2, 3, 4}
#
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集，并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
# s1 & s2 -------------->{2, 3}
# s1 | s2 ------------------>{1, 2, 3, 4}
# s1.add([1, 2, 3]) ------------>TypeError: unhashable type: 'list'
# set 和 dict 的唯一区别仅在于没有存储对应的value 但是set和dict的原理一样，所以同样不可以放入可变对象，因为无法判断两个对象是否相等，也就无法保证set内部“不会有重复的元素”
#
#
#
# 再议不可变对象
# 不可变对象 即基础数据类型，原理基本上与java一样
# 对于不变对象来说，调用对象自身的任意方法，也不会改变该对象自身的内容。相反，这些方法会创建新的对象并返回，这样，就保证了不可变对象本身永远是不可变的。
#
# tuple是不可变对象
s1 = set([1, 2, 3])
s1.add((1, 2, 3))
# s1-------------->{1, 2, 3, (1, 2, 3)}
# s1.add((1, 2, [1, 2, 3]))-------------->TypeError: unhashable type: 'list'
#
#
#
#
#
# 总结 list tuple dict set
# 关于表示：
# list:['a', 'b', 'c'],['a', 'c', ['q', 'c'], 'b;]
# tuple:('q', 'b', 'c'),('s', 'c', ['a', 'b', 'e']),当t=(1),时会被认为是 t=1,因此为了防止歧义则用t=(1,)表示
# dict:{'a' : 12,'Ma' : 123,'xv' : 'Hello','t' : ['1', 1, 3]}，set中的key
# set : {'1w', 'cs', 'sf'} 创建set需要一个list s = set(['q', 'w', 'c'])
# 关于添加元素：
# list:
#       追加:a.append(xs)
#       插入指定位置：a.insert(1,"asdf")
# tuple:
#        tuple一经初始化之后，元素便不能再修改，所以没有添加方法，但是tuple元素内部的引用类型的变量的内容是可以修改的.
# dict:
#       dict内的添加是无序的，dict的底层是Hash表，所以key不能重复
#       添加方式为：d['ase'] = 123
# set:
#      s.add(123)    set可以看成集合，所以也不能重复
# 关于删除元素：
#   list:
#       l.pop(index)
#   tuple:
#         tuple初始化后便不能修改，因此不能删除
#   dict:
#       d.pop(k)
#   set:
#       s.remove(element)
# 关于查询元素：
#   list:
#       用索引 l[0],l[1],l[-1],如果访问list中的list 的变量，用二级索引
#   tuple:
#       同上，t[1],t[2]
#   dict：
#       value = d[key]
#   set:
#       暂时不知道怎么获取单个元素
#
# 关于元素的修改
#   list:
#       用索引,l[index] = value
#   tuple:
#        初始化后不能修改
#   dict:
#       直接赋值，就会把原来的元素冲掉。d[key] = value
#   set:
#       不能修改单个值,可以删除后重新添加。
#
