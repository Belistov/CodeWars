## SUCCESS ##

def solution(text, ending):
    common = False
    text=text.upper()
    ending=ending.upper()
    if text.endswith(ending):
        common = True
    else:
        pass
    return common


a,b = map(str, input().split())
c = solution(a,b)
print(c)