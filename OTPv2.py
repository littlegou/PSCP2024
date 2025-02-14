"""OTP"""
def four(n):
    """four"""
    lis = []
    for i in range(10):
        if n.count(str(i))>0:
            lis.append(n.count(str(i)))
    lis.sort(reverse=True)
    if lis[0] == 2 and lis[1] != 2:
        return "Valid"
    return "Invalid"
def six(n):
    """six"""
    lis = []
    for i in range(10):
        if n.count(str(i))>0:
            lis.append(n.count(str(i)))
    count = 0
    count3 = 0
    for i in lis:
        if i == 3:
            count3 += 1
        if i == 2:
            count += 1
    if count == 2 or count3 == 1:
        return "Valid"
    return "Invalid"
def eight(n):
    """eight"""
    lis = []
    for i in range(10):
        if n.count(str(i))>0:
            lis.append(n.count(str(i)))
    count2 = 0
    count3 = 0
    for i in lis:
        if i ==3:
            count3 += 1
        elif i == 2:
            count2 += 1
    if count3 == 2 or count2==3:
        return "Valid"
    return "Invalid"
def main(n):
    """main"""
    ans = []
    while n != "0":
        if len(n) == 4:
            ans.append(four(n))
        elif len(n) == 6:
            ans.append(six(n))
        elif len(n) == 8:
            ans.append(eight(n))
        n = input()
    print(*ans,sep="\n")
main(input())
