"""BreachTheDoor"""
def main(n):
    """main"""
    lis = n.split()
    count = 0
    newlis = []
    for i in lis:
        for j in i:
            if j.isalpha():
                count += 1
        if count>6:
            newlis.append(i)
        count = 0
    ans = " ".join(newlis)
    for i in ans:
        if i.isalpha() or i.isspace():
            print(i,end="")
main(input())
