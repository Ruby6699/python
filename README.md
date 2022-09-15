Use the print function and loop structure to output a Pyramid consisting of *.
    *
   ***
  *****
 *******
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
