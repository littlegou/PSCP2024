"""[Final 2019] IP Address"""
def main(ip):
    """[Final 2019] IP Address"""
    if len(ip) != 4:
        print("Invalid IPv4 address")
        return
    ans = ""
    for i in ip:
        if i.isnumeric() and 0<= int(i) <= 255:
            ans += str(int(i)) + '.'
        else:
            print("Invalid IPv4 address")
            return
    print(ans.strip("."))
main(input().split("."))
