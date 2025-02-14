"""[Extra From Prepro67] Minesweeper"""
def add(lis,i,j):
    """cal"""
    if 0 <= i-1 <= len(lis)-1 and 0 <= j-1 <= len(lis[0])-1 and lis[i-1][j-1] != "*":
        lis[i-1][j-1] = int(lis[i-1][j-1]) + 1
    if 0 <= i-1 <= len(lis)-1 and lis[i-1][j] != "*":
        lis[i-1][j] = int(lis[i-1][j]) + 1
    if 0 <= i-1 <= len(lis)-1 and 0 <= j+1 <= len(lis[0])-1 and lis[i-1][j+1] != "*":
        lis[i-1][j+1] = int(lis[i-1][j+1]) + 1
    if 0 <= j-1 <= len(lis[0])-1 and lis[i][j-1] != "*":
        lis[i][j-1] = int(lis[i][j-1]) + 1
    if 0 <= j+1 <= len(lis[0])-1 and lis[i][j+1] != "*":
        lis[i][j+1] = int(lis[i][j+1]) + 1
    if 0 <= i+1 <= len(lis)-1 and 0 <= j-1 <= len(lis[0])-1 and lis[i+1][j-1] != "*":
        lis[i+1][j-1] = int(lis[i+1][j-1]) + 1
    if 0 <= i+1 <= len(lis)-1 and lis[i+1][j] != "*":
        lis[i+1][j] = int(lis[i+1][j]) + 1
    if 0 <= i+1 <= len(lis)-1 and 0 <= j+1 <= len(lis[0])-1 and lis[i+1][j+1] != "*":
        lis[i+1][j+1] = int(lis[i+1][j+1]) + 1
    return lis
def main(m):
    """[Extra From Prepro67] Minesweeper"""
    matrix = [input().split() for _ in range(int(m[1]))]
    for i in range(int(m[1])):
        for j in range(int(m[0])):
            if matrix[i][j] == "*":
                matrix = add(matrix,i,j)
    for i in matrix:
        print(*i)
main(input().split(" x "))
