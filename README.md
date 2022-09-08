
1. List deduplication, implemented with for loop
```
list1 = [11,22,33,44,44,33,22,55,66,77,88,99]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
```
2. A shopping mall is on sale, all original prices are integers, if the purchase price is between $50 - 100(including $50 and $100),it
will give a 10% discount; if the purchase price is more than $100, it will give a 20% discount. Write a program that asks for the purchase price and displays the discount and final price.
```
price = int(input('purchase price：')
if 50 <= price <= 100:
    print(f'''
    discount：90%
    dicounted price：{price*0.9}''')
elif price>100:
    print(f'''
    discount：80%
dicounted price：{price * 0.8}
''')
else:
    print("no discount")
```
3. Find the Maximum of Three Integers
```
a1=679
a2=89
a3=90
if a1>a2 and a1>a3:
    print(a1)
elif a2>a1 and a2>a3:
    print(a2)
else:
    print(a3)
```
4. Use python to find the daffodils number from 100 to 999. The daffodil number is a 3-digit positive integer.
The sum of each number raised to the power of 3 is equal to itself.
For example: 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3
153 is a three-digit number, and the sum of the cubes of each number is equal to 153.
```
for n in range(100,1000):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if n == a**3+b**3+c**3:
        print(n)
```
5. Output 99 multiplication table.
The format is as follows:
1 * 1 = 1

1 * 2 = 2 2 * 2 = 4

1 * 3 = 3 2 * 3 = 6 3 * 3 = 9

1 * 4 = 4 2 * 4 = 8 3 * 4 = 12 4 * 4 = 16

1 * 5 = 5 2 * 5 = 10 3 * 5 = 15 4 * 5 = 20 5 * 5 = 25

1 * 6 = 6 2 * 6 = 12 3 * 6 = 18 4 * 6 = 24 5 * 6 = 30 6 * 6 = 36

1 * 7 = 7 2 * 7 = 14 3 * 7 = 21 4 * 7 = 28 5 * 7 = 35 6 * 7 = 42 7 * 7 = 49

1 * 8 = 8 2 * 8 = 16 3 * 8 = 24 4 * 8 = 32 5 * 8 = 40 6 * 8 = 48 7 * 8 = 56 8 * 8 = 64

1 * 9 = 9 2 * 9 = 18 3 * 9 = 27 4 * 9 = 36 5 * 9 = 45 6 * 9 = 54 7 * 9 = 63 8 * 9 = 72 9 * 9 = 81
```
for row in range(1,10):
    for num in range(1,row+1):
        print(f'{num}*{row}={num*row}',end = '\t')
    print()

```
