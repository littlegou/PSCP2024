"""Saint Seiya"""
def main(sec,punch):
    """main"""
    ans = 0
    for i in range(2,sec+1,2):
        if ans>=punch:
            ans += (sec-i+1)*12
            break
        if not i%6:
            ans += 1
        elif not i%2:
            ans += 165
    print(ans)
main(int(input()),int(input()))
