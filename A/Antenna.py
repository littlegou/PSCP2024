"""Antenna"""
import json
def main(r,lis):
    """Antenna"""
    count = 0
    while lis:
        lis = list(filter(lambda x:x>lis[0]+r*2,lis))
        count += 1
    print(count)
main(int(input()),sorted(json.loads(input())))
