"""PongYa"""
def main():
    'pep8'
    num = int(input())
    if not num%3 or str(num)[-1] == '3':
        print('PONG')
    else:
        print(num)
main()
