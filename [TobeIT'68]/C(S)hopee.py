"""C(S)hopee"""
def main(k,l,m,n):
    """main"""
    if k >= l:
        st = k
    else:
        st = k + m
    nd = (m+k)*(1-(n/100))
    if st<=nd:
        print(1)
        print(st)
    else:
        print(2)
        print(nd)
main(float(input()),float(input()),float(input()),float(input()))
