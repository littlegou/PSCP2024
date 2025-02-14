"""[Final 2020] Pad Thai"""
def main(sen):
    """[Final 2020] Pad Thai"""
    ing = set()
    ching = {"Pad Thai Sauce","Tofu","Pickle Turnip","Shrimp","Bean Sprouts","Noodle",\
             "Chives","Lime","Egg","Oil","Peanuts"}
    bad = 0
    while sen != "Cook":
        ing.add(sen)
        bad += 1 if sen not in ching else 0
        sen = input()
    t = set()
    cht = {"Sweet","Sour","Salty"}
    while sen != "End":
        sen = input()
        if sen != "End":
            t.add(sen)
    if ing == ching and t == cht:
        print("Delicious!")
    elif ing == ching:
        print("Not Bad...")
    elif bad:
        print("This is not Pad Thai!!!")
    elif not bad:
        print("This is bad!")
main(input())
