shoplist = ['apple','what']
print('i have ',len(shoplist),'to buy')
print('th item is ',end = ' ')
for item in shoplist:
    print(item,end = ' ')
print('also buy other')
shoplist.append('rice')
print(shoplist)
print('sort')
shoplist.sort()
print('after sort')
print(shoplist)
print('the first is ',shoplist[0])
del shoplist[0]
print(shoplist)
for item in shoplist:
    print(item,end = ' ')   #这样打印就不会带着括号，只是打印元素
print(shoplist)     #直接打印会带着中括号和单引号
