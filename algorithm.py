n = int(input())
result = ""

while n > 0:
    num = n % 2
    result += str(num)
    n = n // 2

print(result[::-1])