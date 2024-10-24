"""Rabbit"""
def main(x,y,n):
    """Rabbit"""
    a = int((y*2)**0.5)
    if y-(a*(a+1))/2 < 0:
        a -= 1
    m = min(a,x,n)
    print("Ahhahaha" if not x-m and not y-(m*(m+1))/2 and not n-m \
          else f"{x-m} {int(y-(m*(m+1))/2)} {n-m}")
main(int(input()),int(input()),int(input()))
