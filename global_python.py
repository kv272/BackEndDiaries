foo = 1
def func():
    global foo
    foo = 2
func()
print(foo)