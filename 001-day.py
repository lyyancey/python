# Python中的字符串是immutable的，所以不能直接修改字符串的某一部分
# 但是可以通过切片的方式来合成一个新的字符串
# 例如：s = 'hello' s = s[:3] + 'p' + s[4:]

# if 语句

def if_section():
    x = int(input("Please enter an integer:"))
    if x < 0:
        x = 0
        print('Negative changed to zero!') # 这里不会继续向下执行
    elif x == 0:
        print('Zero')
    elif x == 1:
        print('Single')
    else:
        print('More')
def for_section():
    
    users = {'Hans': 'active', 'Eleonore': 'inactive', 'Karl': 'active', 'Ludwig': 'inactive'}
    # 如果需要在迭代中修改序列，比较简单的方法是迭代这个序列的副本
    for user,  status in users.copy().items():
        if status == 'inactive':
            del users[user]
    
    active_users = {}
    for user, status in users.items():
        if status == 'active':
            active_users[user] = status
    
    print(active_users)
    print(users)
# 列表也可以进行大小的比价
def range_section():
    x = [1, 2, 3]
    y = [1, 2, 3, 2]
    if x < y:
        print('x is less than y')
    else:
        print('x is greater than y')
# 循环中的break、continue和else
def break_continue_else():
    for x in range(2, 10):
        for n in range(2, x):
            if x % n == 0:
                print(x, 'equals', n, '*', x//n)
                break
        else:
            print(x, 'is a prime number')
    # else子句只有在循环正常结束时才会执行，而不是在循环被break时执行

# match 语句 需要在3.10版本以上
def match_section(status):
    """     match status:
        case 400:
            print('Bad request')
        case 500:
            print('Internal server error')
        case 418:
            print('I am ateapot')
        case _:
            print("Something's wrong with the internet! ") """
    pass
# 函数
def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()

# 函数定义的详细解释
## 默认值参数
def ask_ok(prompt, retries=4, reminder="Please try again!"):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

def f(a, L=[]):
    L.append(a)
    return L
# 如果不想让默认值在后续调用中共享，可以使用None作为默认值，并在函数体中重新赋值
def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

'''关键字参数'''
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print('if you put', voltage, 'vlots through it.')
    print('-- Lovely plumage, the', type)
    print("-- It's", state, "!")

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("*"*40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# 特殊参数
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# 解包参数列表
# 列表用*解包
# 字典用**解包
    
if __name__ == '__main__':
    # if_section()
    # for_section()
    # range_section()
    # break_continue_else()
    # match_section(500)
    # fib(2000)
    # f = fib  # 函数可以赋值给变量
    # print(f) # <function fib at 0x000001EB21276CA0>
    # f(100)
    """     ask_ok('Do you really want ot quit?')
    ask_ok('OK to overwrite the file?', 2)
    ask_ok('OK to overwrite the file?', 2, 'Come on only yes or no!') """

    """     i = 5
    def f(arg=i):
        print(arg)
    i = 6
    f() """
    """
    [1]
    [1, 2]
    [1, 2, 3]
    [1, 2, 1, 4]
    [1, 2, 3, 5]
    """
    """ print(f(1))
    print(f(2))
    print(f(3))
    print(f(4, L=[1,2,1]))
    print(f(5)) """
    '''
    [1]
    [2]
    [3]
    [1, 2, 1, 4]
    [5]
    '''
    """     print(ff(1))
    print(ff(2))
    print(ff(3))
    print(ff(4, L=[1,2,1]))
    print(ff(5)) """
    # parrot(1000, action='VOOOOOM')
    """ cheeseshop(
        'Limburger',
        'It\'s very runny, sir.',
        'It\'s really very, VERY runny, sir.', 
        shopkeeper='Michael Palin',
        client='John Cleese',
        sketch='Cheese Shop Sketch') """
    standard_arg(2)
    standard_arg(arg=3)

    pos_only_arg(2)
    combined_example(3, standard=2, kwd_only=1223)