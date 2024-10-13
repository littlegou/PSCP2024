"""BookWorm"""
def main(wf):
    """main"""
    ans = []
    i = 0
    while i < wf:
        lis = []
        time = float(input())
        book = int(input())
        for _ in range(book):
            lis.append(float(input()))
        lis.sort()
        while True:
            if sum(lis)<=time:
                ans.append(len(lis))
                break
            lis = lis[:-1]
        i += 1
    for i in ans:
        print(i)
main(int(input()))
