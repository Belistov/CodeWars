## SUCCESS ##

def disemvowel(comment):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    clear = ''
    for char in comment:
        if char not in vowels:
            clear += char
    return clear

comment=input()
printer = disemvowel(comment)
print(printer)

