"""[Final 2021] Poisonous Vegetables"""
def main(veg,area,_):
    """[Final 2021] Poisonous Vegetables"""
    for _ in range(int(veg[0])):
        x = input()[:-1].replace("[","").split("]")
        for j in range(int(veg[1])):
            v = x[j].split()
            if int(v[1]) > area:
                print("[ - ]",end="")
            elif int(v[0]) != int(v[2]):
                print("[ x ]",end="")
            else:
                print("[ o ]",end="")
        print()
main(input().split(" x "),int(input()),int(input()))
