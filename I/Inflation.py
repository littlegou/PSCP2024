"""Inflation"""
def main(n,k):
    """main"""
    if not k or not n:
        print(f"{n:.2f}")
    else:
        if n - int(n):
            n = int(n*100)*10381
            n = str(n)[:-4]
        else:
            n = int(n)*10381
            n = str(n)[:-2]
        n = int(n)
        for _ in range(1,k):
            n = (n*10381)//10000
        a = str(n)[:-2]
        b = str(n)[-2:]
        if not a:
            a = 0
        if len(b)<2:
            b = f"{b:>02}"
        print(str(a)+"."+str(b))
main(float(input()),int(input()))
