func = lambda x:((x+5)*3)//2
a = [8,6,14,37,23,9,20,10]
#iterator = list(range(len(a)))
new_list = list(map(func,a))
print (new_list)