"""Fever"""
def check(valuet):
    """check"""
    if 36<=valuet<38:
        return 'No Fever'
    if 38<=valuet<39:
        return 'Mild Fever'
    if 39<=valuet<40:
        return 'High Fever'
    if valuet>=40:
        return 'Very High Fever'
    return None
def main():
    """cal"""
    x = float(input())
    print(check(x))
main()
