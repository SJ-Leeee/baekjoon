product = 1
for _ in range(3):
    num = int(input())
    product *= num

dictionary = {}
product_str = str(product)
for num in product_str:
    if num in dictionary:
        dictionary[num] += 1
    else:
        dictionary[num] = 1

for i in range(10):
    key = dictionary.get(str(i)) or 0
    print(f"{key}")
