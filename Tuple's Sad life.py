"""Tuple's Sad life"""
def main(tp,f):
    """main"""
    a = tp.replace(" ","")
    w = a.find(f)
    wg = a.count(f)
    for _ in range(wg):
        for _ in range(wg):
            print(str(w)+" ",end = '')
        print()
main(input(),input())
