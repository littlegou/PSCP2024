"""Supercar Parking"""
import math
def main(lis):
    """Supercar Parking"""
    num = lis.split("1")
    ans = 0
    if "1" not in lis:
        print(math.ceil(len(num[0])/2))
    else:
        for i,j in enumerate(num):
            if (j and not i) or (j and i == len(num)-1):
                ans += math.floor(len(j)/2)
            elif j:
                if not len(j)%2:
                    ans += math.floor(len(j)/2)-1
                else:
                    ans += math.floor(len(j)/2)
        print(ans)
main(input())
