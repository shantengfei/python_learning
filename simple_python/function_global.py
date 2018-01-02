# x=50
# def func(x):
#     print('x is ',x)
#     # global x
#     x=2
#     print("x is ",x)
#     x=2
#     print('changed global x to',x)
#
# func(x)
# print('value x is',x)

x=50
def func():
    # print('x is ',x)
    global x
    x=2
    print("x is ",x)
    x=2
    print('changed global x to',x)

func()
print('value x is',x)
