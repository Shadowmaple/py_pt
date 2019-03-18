from functools import wraps
import time

def param(name):
    def test(func):
        @wraps(func)
        def x(*args, **kwargs):
            t = time.strftime('%H:%M:%S', time.localtime())
            print('It\'s {} now.'.format(t))
            print('I am {}.'.format(name))
            return func(*args, **kwargs)
        return x
    return test

@param('Shadow')
def foo(name='Nick', ):
    print("Hello, I'm %s." %name)

if __name__ == '__main__':
    foo('Mark')
