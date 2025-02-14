"""TicTacToe"""
def main():
    """main"""
    lis = []
    for _ in range(3):
        lis.append(input())
    if lis[0][0] == lis[1][1] == lis[2][2] and lis[0][0] != "-":
        print(lis[0][0] , "WIN")
    elif lis[0][0] == lis[0][1] == lis[0][2] and lis[0][0] != "-":
        print(lis[0][0] , "WIN")
    elif lis[0][0] == lis[1][0] == lis[2][0] and lis[0][0] != "-":
        print(lis[0][0] , "WIN")
    elif lis[1][0] == lis[1][1] == lis[1][2] and lis[1][0] != "-":
        print(lis[1][0] , "WIN")
    elif lis[2][0] == lis[2][1] == lis[2][2] and lis[2][2] != "-":
        print(lis[2][0] , "WIN")
    elif lis[0][1] == lis[1][1] == lis[2][1] and lis[0][1] != "-":
        print(lis[0][1] , "WIN")
    elif lis[0][2] == lis[1][2] == lis[2][2] and lis[0][2] != "-":
        print(lis[0][2] , "WIN")
    elif lis[0][2] == lis[1][1] == lis[2][0] and lis[0][2] != "-":
        print(lis[0][2] , "WIN")
    else:
        print("DRAW")
main()
