"""Kaprekar"""
def findnop(x):
    """a"""
    lis = list(str(x))
    new = []
    while lis:
        mi = lis[0]
        for i in lis:
            if i < mi:
                mi = i
        new.append(mi)
        lis.remove(mi)
    ans = "".join(new)
    if len(ans)<4:
        ans = f"{ans:>04}"
    return ans
def findnma(x):
    """a"""
    lis = list(str(x))
    new = []
    while lis:
        mi = lis[0]
        for i in lis:
            if i > mi:
                mi = i
        new.append(mi)
        lis.remove(mi)
    ans = "".join(new)
    if len(ans)<4:
        ans = f"{ans:<04}"
    return ans
def main(num):
    """main"""
    count = 0
    while num != 6174:
        num = int(findnma(num)) - int(findnop(num))
        count += 1
    print(count)
main(input())
