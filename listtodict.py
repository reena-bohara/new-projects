letters = ['a','b','c','a','b','c','d','e','a']
result = {} #initializing the result dict
for x in letters:
    result[x] = result.get(x,0)+1
    print("the dict after each variable",result)
print("the final dictionary",result)

