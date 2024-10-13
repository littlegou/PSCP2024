"""Point Sorting"""
def main(n):
    """main"""
    i = 0
    mlis = []
    while i<n:
        slis = []
        for _ in range(int(input())):
            a = input().split()
            results = list(map(int, a))
            slis.append(results)
        slis = sorted(slis, key=lambda x: (sum(x), -x[1]))
        mlis.append(slis)
        i += 1
    for i in range(n):
        for j in mlis[i]:
            print(str(j[0])+ " " +str(j[1]))
main(int(input()))
