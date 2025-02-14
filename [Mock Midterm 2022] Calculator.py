"""Calculator"""
def main(x):
    """Calculator"""
    hm = 0
    for i in range(1,x+1):
        for _ in str(i):
            hm += 1
        hm += 1
    if x == 1:
        print(1)
    else:
        print(hm)
main(int(input()))
