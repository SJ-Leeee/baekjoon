num1, num2 = map(int, input().split())

str1 = int(str(num1)[::-1])
str2 = int(str(num2)[::-1])

result = str1 if str1 > str2 else str2
print(result)