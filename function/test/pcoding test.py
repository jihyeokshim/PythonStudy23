# E7-1
def func():
    x = 200


func()


# E7-2
def func():
    x = 200
    print(x)


x = 100
func()
print(x)


# E7-3
def func():
    global x
    x = 200
    print(x)


x = 100
func()
print(x)
