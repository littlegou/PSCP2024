"""War"""
def main(lis1,lis2):
    """War"""
    lis1.sort(reverse=True)
    lis2.sort(reverse=True)
    ans = 0
    for i in lis1:
        l = len(lis2)
        for _ in range(l):
            if i > lis2[0]:
                ans += i
                lis2.remove(lis2[0])
                break
            lis2.remove(lis2[0])
    print(ans)
main(list(map(int,input()[1:-1].split(", "))),list(map(int,input()[1:-1].split(", "))))
