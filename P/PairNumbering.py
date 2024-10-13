"""PairNumbering"""
import json
def main(lisa,lisb,p):
    """main"""
    lisa = json.loads(lisa)
    lisb = json.loads(lisb)
    count = 0
    for i in lisa:
        if p - i in lisb:
            count += lisb.count(p - i)
    print(count)
main(input(),input(),int(input()))
