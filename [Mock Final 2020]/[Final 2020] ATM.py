"""[Final 2020] ATM"""
def main(money,sen):
    """[Final 2020] ATM"""
    while sen != "END":
        if sen[0] == "D":
            money += int(sen[2:])
        elif sen[0] == "W":
            money -= int(sen[2:]) if (int(sen[2:]) - money < 0) else money
        sen = input()
    print(money)
main(int(input()),input())
