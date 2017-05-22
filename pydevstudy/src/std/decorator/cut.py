'''
Created on May 6, 2017

@author: zhai
'''

def before(f):
    def wrapper():
        print('before function')
        f()
    return wrapper

def after(f):
    def wrapper():
        f()
        print('after function')
    return wrapper

@before
@after
def func():
    print('this is function')
    
    
def decorator(func):
    print("hello")
    return func

@decorator
def foo():
    pass

def decorator_with_params(arg_of_decorator):#这里是装饰器的参数
    print(arg_of_decorator)

@decorator_with_params("deco_args")
def foo3():
    pass
  
if __name__ == '__main__':
    foo()
    func()
    
    foo3()
    