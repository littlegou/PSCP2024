"""Netflix"""
import math
def main(screen,downl,_,__,wtv,hd,ultra):
    """main"""
    ans = 0
    while screen>0 or downl > 0:
        if ultra == "Yes" or ((screen >= 3 or downl >= 3) and (wtv == "Yes" or hd == "Yes")):
            num = max(math.ceil(screen / 4), math.ceil(downl / 4))
            if max(screen,downl)%4>2 or not max(screen,downl)%4 or ultra == "Yes":
                print(f"Premium x {num}")
                ans += (num)*419
                screen -= 4*num
                downl -= 4*num
            else:
                num = max(math.ceil(screen/4),math.ceil(downl/4),2)
                print(f"Premium x {num-1}")
                ans += (num-1)*419
                screen -= 4*(num-1)
                downl -= 4*(num-1)
        elif hd == "Yes" or ((screen>=2 or downl>=2) and wtv == "Yes"):
            num = max(math.ceil(screen/2),math.ceil(downl/2))
            print(f"Standard x {num}")
            ans += num*349
            screen -= 2*num
            downl -= 2*num
        elif wtv == "Yes":
            print(f"Basic x {max(screen,downl)}")
            ans += (max(screen,downl))*279
            screen -= 1
            downl -= 1
        else:
            print(f"Mobile x {max(screen,downl)}")
            ans += max(screen,downl)*99
            break
    print(f"Total = {ans} THB")
main(int(input()),int(input()),input(),input(),input(),input(),input())
