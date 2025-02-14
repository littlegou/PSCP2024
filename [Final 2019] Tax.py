"""[Final 2019] Tax"""
def main(y,cc):
    """main"""
    if cc > 1800:
        paid = 2100 + (cc - 1800)*4
    elif cc > 600:
        paid = 300 + (cc - 600)*1.5
    else:
        paid = cc * 0.5
    if y >= 10:
        print(f"{paid*0.5:.2f}")
    elif y >= 9:
        print(f"{paid*0.6:.2f}")
    elif y >= 8:
        print(f"{paid*0.7:.2f}")
    elif y >= 7:
        print(f"{paid*0.8:.2f}")
    elif y >= 6:
        print(f"{paid*0.9:.2f}")
    else:
        print(f"{paid:.2f}")
main(float(input()),float(input()))
