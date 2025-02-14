"""[Recommend] Heads and Legs"""
def main(a,b):
    """[Recommend] Heads and Legs"""
    bi = -(2*a-b)/2
    print(f"{int(bi)} {int(a-bi)}" if a-bi >=0 and bi >= 0 and bi.is_integer() else "Impossible")
main(int(input()),int(input()))
