"""BookWorm"""
def main(wf):
    """main"""
    ans = []
    i = 0
    while i < wf:
        time = float(input())
        book = int(input())
        tr = 0
        count = 0
        futureans = 0
        for j in range(1,book+1):
            tim = float(input())
            if tr+tim > time and not count:
                futureans = j+1
                count = 1
            elif count:
                pass
            else:
                tr += tim
        if tr>0 and not futureans:
            ans.append(1)
        elif futureans:
            ans.append(futureans)
        elif tr<time:
            ans.append(book)
        i += 1
    for i in ans:
        print(int(i))
main(int(input()))
