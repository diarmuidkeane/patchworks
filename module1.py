
def module_method1():
    pass

class A:
    def methodA(self,pos1):
        module_method1()

def module_method2():
    a= A()
    a.methodA('arg1')


class B:
    def __init__(self) -> None:
        pass

    def methodB(self):
        A().methodA('argB')
    
