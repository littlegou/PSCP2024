""" SecondConverter """
def main():
    """ SecondConverter """
    k = int(input())
    s = int(input())
    m = int(input())
    h = int(input())
    ans = k%((s*m)*h)
    hour = ans//(m*s)
    x = ans%(m*s)
    minute = x//s
    seconds = x%s
    print(f"{hour}:{minute}:{seconds}")
main()
