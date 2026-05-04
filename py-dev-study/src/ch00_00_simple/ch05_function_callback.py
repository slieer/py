'''
Created on Apr 11, 2015

@author: dev
'''

def my_callback(input_):
    print("function my_callback was called with %s input" % (input,))

def caller(input_, func):
    func(input_)

if __name__ == "__main__" :
    for i in range(5):
        caller(i, my_callback)
