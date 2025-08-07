def first(s):
    return s[0]

def rest(s):
    return s[1]

def link(first,rest):
    return [first,rest]

def extend_link(s,t):
    if s == 'empty':
        return t
    
    else:
        return link(first(s),extend_link(rest(s),t))

def getitem_link(s,i):
    while i > 0:
        s, i = rest(s), i - 1
    return print(first(s))

def apply_to_all_link(f,s):
    if s == 'empty':
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))


four = [1,[2,[3,[4, 'empty']]]]
#getitem_link(four,3)
extend_list = extend_link(four,[20,[40,[-1,[-2,[-3,'empty']]]]])
print(extend_list)
func_11 = apply_to_all_link(lambda x:x*x, extend_list)
print(func_11)