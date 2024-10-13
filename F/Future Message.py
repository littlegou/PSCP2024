"""Future Message"""
def main():
    """fm"""
    x = input()
    if x.isnumeric():
        print("Number")
    elif x.isupper():
        print("Uppercase")
    elif x.islower():
        print("Lowercase")
    elif x.istitle():
        print("Title")
    elif x.isspace():
        print("Space")
    else:
        print("Other")
main()
