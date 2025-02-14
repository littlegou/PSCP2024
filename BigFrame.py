"""BigFrame"""
def main(a,b,c,d,e):
    """main"""
    length = max(len(a.strip()),len(b.strip()),len(c.strip()),len(d.strip()),len(e.strip()))
    print("*"*(length+4))
    print("* "+f"{a.strip():<{length}}"+" *")
    print("* "+f"{b.strip():<{length}}"+" *")
    print("* "+f"{c.strip():<{length}}"+" *")
    print("* "+f"{d.strip():<{length}}"+" *")
    print("* "+f"{e.strip():<{length}}"+" *")
    print("*"*(length+4))
main(input(),input(),input(),input(),input())
