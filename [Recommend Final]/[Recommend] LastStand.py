"""[Recommend] LastStand"""
import json
def main(lis):
    """[Recommend] LastStand"""
    print("\n".join([str(i%10) for i in lis]))
main(json.loads(input()))
