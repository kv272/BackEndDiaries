foo = 1
def func():
    global foo
    foo = 2
def func2():
    print("what's done is done")
func()
print(foo)