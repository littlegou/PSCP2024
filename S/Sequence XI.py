"""Sequence XI"""
def main(n):
    """main"""
    for i in range(1,n):
        oth = ""
        a = 1
        b = i
        for _ in range(1,n*2-1):
            if a<i:
                oth += f"{a:>02} "
                a += 1
            elif a == i:
                for _ in range(1,(n*2)-(2*(i-1))-1):
                    oth += f"{a:>02} "
                a+=1
            else:
                if b>=1:
                    oth += f"{b:>02} "
                    b -= 1
        print(oth)
    for i in range(n,1,-1):
        oth = ""
        a = 1
        b = i
        for _ in range(n*2,0,-1):
            if a<i:
                oth += f"{a:>02} "
                a += 1
            elif a == i:
                for _ in range(1,(n*2)-(2*(i-1))-1):
                    oth += f"{a:>02} "
                a+=1
            else:
                if b>=1:
                    oth += f"{b:>02} "
                    b -= 1
        print(oth)
    print("01 "*(n*2-1))
main(int(input()))
