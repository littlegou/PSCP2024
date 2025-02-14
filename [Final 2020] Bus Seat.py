"""[Final 2020] Bus Seat"""
def main(row,seat,xx):
    """[Final 2020] Bus Seat"""
    lis = []
    xx = f"{xx:>02}"
    for j in range(1,row+1):
        lis.append([f"{j + i*row:>02}" if f"{j + i*row:>02}" != xx else "XX" for i in range(seat)])
    for i,j in enumerate(lis[::-1]):
        print(*j)
        if i%2 and i != row-1:
            print()
main(int(input()),int(input()),int(input()))
