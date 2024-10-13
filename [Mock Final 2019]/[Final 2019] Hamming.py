"""Ham"""
def main():
    """main"""
    s1 = list(input())
    s2 = list(input())
    l = len(s1)
    count = 0
    for i in range(l):
        if s1[i] != s2[i]:
            count += 1
    print(count)
main()
