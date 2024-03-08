def testException():
    # 异常
    class B(Exception):
        pass
    class C(B):
        pass

    class D(C):
        pass

    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

def testException2():
    import sys
    try:
        f = open('hello.py')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("OS error: ", err)
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print(f"Unexcepted error {err=}, {type(err)=}")
        raise

""" def testException3():
    excs = [OSError('error 1'), SystemError('error 2')]
    raise ExceptionGroup(excs) """
def scope_test():
    def do_local():
        spam = "local spam"
    
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"
    
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

if __name__ == "__main__":
    # testException()
    # testException2()
    # testException3()
    
    # scope_test()
    # print("In global scope:", spam)
    rev = Reverse('spam')
    for char in rev:
        print(char)
    print(rev.__doc__)