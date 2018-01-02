dict={'a':1,'b':2,'c':3}
print('c is',dict['c'])
del dict['c']
print('length is {}'.format(len(dict)))
for name,address in dict.items():
    print('{} is {}'.format(name,address))
dict['f']=5
