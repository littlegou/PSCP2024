"""[Recommend] Diamond I"""
def main(m,n):
    """[Recommend] Diamond I"""
    lis = [0 for _ in range(n)]
    for _ in range(m):
        inp = input().split()
        for j in range(n):
            lis[j] += int(inp[j])
    print(max(lis))
main(int(input()),int(input()))
