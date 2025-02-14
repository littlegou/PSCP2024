"""[Final 2021] Dancing"""
from math import floor
def cal(x,y,dance,stage):
    """cal"""
    if dance == "North":
        x -= 1*(0<=x-1<stage)
    elif dance == "Northeast":
        x -= 1*(0<=x-1<stage)
        y += 1*(0<=y+1<stage)
    elif dance == "Northwest":
        x -= 1*(0<=x-1<stage)
        y -= 1*(0<=y-1<stage)
    elif dance == "East":
        y += 1*(0<=y+1<stage)
    elif dance == "Southeast":
        x += 1*(0<=x+1<stage)
        y += 1*(0<=y+1<stage)
    elif dance == "South":
        x += 1*(0<=x+1<stage)
    elif dance == "Southwest":
        x += 1*(0<=x+1<stage)
        y -= 1*(0<=y-1<stage)
    elif dance == "West":
        y -= 1*(0<=y-1<stage)
    return x,y
def main(stage,x,bonus):
    """[Final 2021] Dancing"""
    lis = []
    for i in range(stage):
        lis.append([1 if (i*stage)+j != x else bonus for j in range(1,stage+1)])
    score = 0
    x,y = floor(stage/2),floor(stage/2)
    while True:
        dance = input()
        if "dance" in dance.lower():
            score += lis[x][y]
        elif dance == "Ultimately":
            score += lis[x][y]*5
        else:
            x,y = cal(x,y,dance,stage)
        if dance == "Ultimately":
            break
    print("Total point :",score)
main(int(input()),int(input()),int(input()))
