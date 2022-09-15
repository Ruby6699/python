### 1. Use the print function and loop structure to output a Pyramid consisting of *.
```
    *
   ***
  *****
 *******
```
```
for row in range(1,max_level+1):
    space_count = max_level - row
    star_count = row * 2 -1
    for item in range(space_count):
        print(" ",end="")
    for item in range(star_count):
        print("*",end="")
    print()
```
### 2. Add the following dictionaries to the file in rows:

person_info = [
    {
        "name": "john",
        "age": 22,
        "gender": "male",
        "hobby": "learning",
        "motto": "learning makes me hanppy"
    },
    {
        "name": "lili",
        "age": 20,
        "gender": "female",
        "hobby": "running",
        "motto": "running is on the way"
    }
]

#### Finally, get an info.txt file like this:
#### name,age,gender,hobby,motto
#### john, 22, male, learning, learning makes me happy
#### lili, 20, female, running, running is on the way

```
fs = open("info.txt", mode="w", encoding="utf-8")
fs.writelines(["name, ", "age, ", "gender, ", "hobby, ", "motto\n"])
for item in person_info:
    for key, value in item.items():
        item[key] = str(value)
    s = ", ".join(item.values())
    s = s + "\n"
    fs.write(s)

```
