"""[Final 2020 + Recommend] Bus Seat"""
def main(y,x,xx):
    """[Final 2020 + Recommend] Bus Seat"""
    for i in range(y,0,-1):
        a = i
        for _ in range(x):
            print(f"{a:>02} " if a != xx else "XX " ,end="")
            a += y
        print()
        if i%2 and i != 1:
            print()
main(int(input()),int(input()),int(input()))
