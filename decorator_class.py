class Decorator(object):
    def __init__(self, func):
        self.func = func
    def __call__(self, *args, **kwargs):
        print("Before function call")
        result = self.func(*args, **kwargs)
        print("After function call")
        return result
@Decorator
def testfunc():
    print('inside the function')
testfunc()