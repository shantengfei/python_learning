def print_max(x,y):
    '''打印两个字符串中数值最大的数
    这两个数都是整数'''
    x=int(x)
    y=int(y)
    if x<y:
        print(y,'is the max')
    elif x>y:
        print(x,'is the max')
print_max(3,5)
print(print_max.__doc__)