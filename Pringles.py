"""Pringles"""
def main(one,two,thr,fing):
    """main"""
    be4 = two.count(")")
    two = two[fing:]
    af = two.count(")")
    print(be4-af)
    if not af:
        print("None.")
    else:
        print("There are still some left.")
    print(one)
    print(f"{two:>{len(one)+1}}")
    print(thr)
main(input(),input(),input(),int(input()))
