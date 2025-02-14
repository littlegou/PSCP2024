"""[Recommend] Restaurant"""
def main(baht,promo,disc,rec):
    """main"""
    if baht + rec < promo:
        disc = 0
    disc = 1-(disc/100)
    if not rec or not disc:
        print("Yes")
    elif baht == promo:
        if (baht + rec)*disc > baht*disc:
            print(f"No {abs((baht*disc)-((baht + rec)*disc)):.3f}")
        elif (baht + rec)*disc < baht*disc:
            print(f"Yes {abs(((baht + rec)*disc)-(baht*disc)):.3f}")
        else:
            print("Yes")
    else:
        if (baht + rec)*disc>baht:
            print(f"No {abs(baht-((baht + rec)*disc)):.3f}")
        elif (baht + rec)*disc<baht:
            print(f"Yes {abs(((baht + rec)*disc)-baht):.3f}")
        else:
            print("Yes")
main(float(input()),float(input()),float(input()),float(input()))
