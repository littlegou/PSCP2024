"""[Final 2020] Area"""
def main(n):
    """[Final 2020] Area"""
    ans = 0
    for _ in range(n):
        a = input()
        ans += len(a) - a.count(" ")
    print(ans)
main(int(input()))
