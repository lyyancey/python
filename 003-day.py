# 练习python 正则表达式
import re

def practiceRex():
    content = '''苹果，是绿色的
    橘子，是橙色的
    西瓜，是红色的
    葡萄，是紫色的
    乌鸦，是黑色的
    猴子，
    '''
    import re
    p = re.compile(r'，.*')
    for one in p.findall(content):
        print(one)

# 贪婪模式 与 非贪婪模式 ?
def practiceRex2():
    source = '<html><head><title>Test</title>'
    p = re.compile(r'<.*>')
    print(p.findall(source))

# \w 匹配字母数字下划线默认情况下也匹配uniocde字符
def practiceRex3():
    source = '''
    王亚辉
    tony
    刘文武
    '''
    p = re.compile(r'\w{2,4}', re.ASCII)
    print(p.findall(source))

def practiceRex4():
    source = '''
    001- 苹果的价格是 5.00元
    002- 橘子的价格是 3.00元
    003- 西瓜的价格是 10.00元
    004- 葡萄的价格是 15.00元
    005- 乌鸦的价格是 20.00元
    '''
    p = re.compile(r'\d{3}', re.MULTILINE)
    print(p.findall(source))

def practiceRex5():
    source = '''
    001- 苹果的价格是 5.00元.
    002- 橘子的价格是 3.00元
    003- 西瓜的价格是 10.00元
    004- 葡萄的价格是 15.00元
    005- 乌鸦的价格是 20.00元
    '''
    p = re.compile(r'[\d]+[.][\d]+元$', re.MULTILINE)
    print(p.findall(source))

def practiceRex6():
    source = '''橘子，是橙色的
西瓜，是红色的
葡萄，是紫色的
乌鸦，是黑色的'''
    p = re.compile(r'^(.*)(，)', re.MULTILINE)
    for first, last in p.findall(source):
        print(f'{first} {last}')
if __name__ == "__main__":
    #    practiceRex()
    practiceRex6()