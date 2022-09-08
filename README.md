
1. List deduplication, implemented with for loop
```
list1 = [11,22,33,44,44,33,22,55,66,77,88,99]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
```
2. A shopping mall is on sale, all original prices are integers, if the purchase price is between $50 - 100(including 50 yuan and 100 yuan),it
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
