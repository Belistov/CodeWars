## SUCCESS ##

def filter_list(l):
    return [x for x in l if isinstance(x, int)]

l = [1, 2, '3' ,3, 'a', 'b', '4', 'c']
a = filter_list(l)
print(a)  # Output: [1, 2, 3]
