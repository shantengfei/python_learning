def maximum(x,y):
    if x<y:
        return y
    elif x>y:
        return x
    else:
        return 'equal'
x=input('first num')
y=input('second num')
print(maximum(x,y))