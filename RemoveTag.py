"""RemoveTag"""
def main(n):
    """main"""
    lis = n.split('>')
    new = []
    for i in lis:
        if i and i[0] != "<":
            new.append(i)
    l = len(new)
    for i in range(l):
        if new[i].find("<") != -1:
            new[i] = new[i][:new[i].find("<")]
    ans = " ".join(new)
    print(ans.split())
main(input())
