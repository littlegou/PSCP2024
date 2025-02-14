"""[Recommend] TicTacToe"""
def main():
    """[Recommend] TicTacToe"""
    xoxo = [list(input()) for _ in range(3)]
    lis = [[xoxo[i][i] for i in range(3)],[xoxo[2-i][i] for i in range(3)]]
    lis.extend([[xoxo[i][j] for j in range(3)] for i in range(3)])
    lis.extend([[xoxo[j][i] for j in range(3)] for i in range(3)])
    winner = ""
    for i in lis:
        winner = i[0] if (i[0] == i[1] == i[2] and i[0] != "-") else winner
    print(f"{winner} WIN" if winner else "DRAW")
main()
