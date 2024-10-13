"""CaesarV1"""
def main(n,sen):
    """main"""
    for i in sen:
        if i.isalpha() and i.isupper():
            if ord(i)+n<65:
                print(chr(90-(64-(ord(i)+n))),end="")
            elif ord(i)+n>90:
                print(chr((ord(i)+n)-91+65),end="")
            else:
                print(chr(ord(i)+n),end="")
        elif i.isalpha() and i.islower():
            if ord(i)+n<97:
                print(chr(122-(96-(ord(i)+n))),end="")
            elif ord(i)+n>122:
                print(chr((ord(i)+n)-123+97),end="")
            else:
                print(chr(ord(i)+n),end="")
        else:
            print(i,end="")
main(int(input())%26,input())
