"""Nearer"""
def main(alice,bob,ice):
    """main"""
    x = alice - ice
    y = bob - ice
    if abs(x)>abs(y):
        print(f"Bob {abs(y)}")
    elif abs(x)<abs(y):
        print(f"Alice {abs(x)}")
    else:
        print(f"Sundaes {abs(x)}")
main(int(input()),int(input()),int(input()))
