"""Elo"""
def main():
    """main"""
    ra = int(input())
    rb = int(input())
    x = str(input())
    if x == "A":
        y = 1/(1+10**((rb-ra)/400))
        print(f"{y:.2f}")
    elif x =="B":
        z = 1/(1+10**((ra-rb)/400))
        print(f"{z:.2f}")
main()
