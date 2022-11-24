n = int(input())
a = input()
b = input()

if n % 2 == 1:
    a = a.replace('1', '2').replace('0', '1').replace('2', '0')

if a == b:
    print('Deletion succeeded')
else:
    print('Deletion failed')