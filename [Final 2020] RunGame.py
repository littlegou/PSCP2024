"""[Final 2020] RunGame"""
def main(lis):
    """[Final 2020] RunGame"""
    l = len(lis)
    x = 0
    ans = 0
    for i in range(l):
        ans += abs(int(lis[i]) - x)
        x = int(lis[i])
    print(ans)
main(input().split())
