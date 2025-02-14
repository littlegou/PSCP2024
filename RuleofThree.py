"""RuleofThree"""
def main(x):
    """main"""
    nop = 0
    pricemax = 0
    gmax = 0
    for _ in range(x):
        price = float(input())
        g = float(input())
        if (g/price)>nop:
            nop = g/price
            pricemax = price
            gmax = g
        elif (g/price)==nop:
            if pricemax>price:
                pricemax = price
                gmax = g
    print(f"{pricemax:.2f} {gmax:.2f}")
main(int(input()))
