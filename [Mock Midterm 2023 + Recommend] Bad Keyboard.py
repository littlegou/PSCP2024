"""Bad Keyboard"""
def main(sent):
    """main"""
    new = ""
    for i in sent:
        if i == "i":
            new += "o"
        elif i == "o":
            new += "i"
        elif i == "I":
            new += "O"
        elif i == "O":
            new += "I"
        else:
            new += i
    print(new)
main(input())
