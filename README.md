
1. List deduplication, implemented with for loop
```
list1 = [11,22,33,44,44,33,22,55,66,77,88,99]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
```
