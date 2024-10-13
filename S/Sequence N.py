""" Sequence N """
def main():
    """ Sequence N """
    m = int(input())
    for i in range(m):
        for j in range(m):
            if j in (0, m - 1, i):
                print("*" ,end="")
            else:
                print(" " ,end="")
        print()
main()
