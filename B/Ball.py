""" Ball """
def main():
    """ Ball """
    h = float(input())
    num = 0
    while h>=0.01:
        h = h*0.6
        num += 1
    print(num-1)
main()
