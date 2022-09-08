
列表去重

for循环实现

```
list1 = [11,22,33,44,44,33,22,55,66,77,88,99]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
print(list2)
```
