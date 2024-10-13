"""Shorten"""
def main(x):
    """main"""
    yo = x
    ans = str(x)
    seq = 0
    while x != -1:
        x = int(input())
        if yo+1 == x:
            if not seq:
                ans += "-"
            seq += 1
        else:
            if seq >0:
                ans += str(yo)
                seq = 0
            if x!= -1:
                ans += ", " + str(x)
        yo = x
    if ans == "-1":
        pass
    else:
        print(ans.strip())
main(int(input()))
