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
##### name,age,gender,hobby,motto
##### john, 22, male, learning, learning makes me happy
##### lili, 20, female, running, running is on the way

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

### 3. A shopping mall is on sale, all original prices are integers, if the purchase price is between $50 - 100(including 50 yuan and 100 yuan),it will give a 10% discount; if the purchase price is more than $100, it will give a 20% discount. Write a program that asks for the purchase price and displays the discount and final price.
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
### 4. Find the Maximum of Three Integers
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
### 5. Use python to find the daffodils number from 100 to 999. The daffodil number is a 3-digit positive integer.
### The sum of each number raised to the power of 3 is equal to itself.
### For example: 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3
### 153 is a three-digit number, and the sum of the cubes of each number is equal to 153.
```
for n in range(100,1000):
    a = n // 100
    b = n // 10 % 10
    c = n % 10
    if n == a**3+b**3+c**3:
        print(n)
```
### 6. Output 99 multiplication table.
### The format is as follows:
```
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
```
for row in range(1,10):
    for num in range(1,row+1):
        print(f'{num}*{row}={num*row}',end = '\t')
    print()

```
### 7.Define a function: def remove_element(a_list). Remove duplicates from list [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
```
def remove_repeatitive_elements(a_list):
    list1=[]
    for item in a_list:
        if item not in list1:
            list1.append(item)
        print(list1)
my_list = [10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]
remove_repeatitive_elements(my_list)
```
### 8.Define a function to multiply all the numbers entered and take the remainder of 20. The number of numbers entered by the user is uncertain.
```
def deal(*args):
    res = 1
    if args:
        for item in args:
            res *= item
        left = res % 20
        print("The result of taking the remainder of 20 is: {}".format(left))
deal(10,20,30,40,50)
```
### 9.By defining a calculator function, call the function passing in 3 parameters, 2 are the numbers to calculate and 1 is the type of calculation.
#### The calculation types are: 【1】add 【2】subtract 【3】multiply 【4】divide.
#### According to the parameters, select the corresponding operation and return the value of the operation.
```
num = int(input('Please choose one of the following 4 operation：【1】add 【2】subtract【3】multiply 【4】divide:'))
def caculator(a,b):
    if num ==1:
        return a+b
    elif num == 2:
        return a-b
    elif num == 3:
        return a * b
    elif num ==4:
        if b != 0:
            return a/b
        else:
            print('Divisor cannot be 0')
print(caculator(100,200))
print(caculator(1,0))
```
### 10. Encapsulate an employee class:
#### Content: employee name, working years, registered residence city, salary, job name
#### Method 1: Calculate the total annual salary of employees
#### Method 2: Print the name and working years of the employee: The working years of the employee XXX are XX
#### Instantiate 2 employees, and call Method 1 and Method 2 respectively
```
class Employee:
    def __init__(self,name,work_years,born_city,salary,job_name):
        self.name = name
        self.work_years = work_years
        self.born_city = born_city
        self.salary = salary
        self.position_name = job_name
    def tol_salary(self):
        sum = int(self.salary) * 12
        print(f'annual payroll is {sum}')

    def p(self):
        print(f'The working years of {self.name} is {self.work_years}')
        
p1 = Employee('Nova','6','brisbane','13000','engineer')
p1.tol_salary()
p1.p()

p2 = Employee('Edward','10','sydney','20000','senior engineer')
p2.tol_salary()
p2.p()
```

### 11. Define a login test case named class LoginCase.
#### Each instance is a login test case.
#### Attribute: case_name, expected_result,actual_result
#### Method 1: Run the test case
#### Description: There are 2 parameters: username and password.
#### That can log in successfully: Username: py37, password: 666666.
#### Determine whether the login is successful by whether the user name and password are correct or not. Return the actual result.
#### Ps: Non-compliance can be considered: password length is not 6 digits/password incorrect/username is incorrect.
#### Method 2: Compare the expected_result and the actual result.
#### Instantiate 2 test cases, and run the instance (call the method), render the method (call the result)
```
class LoginCase:

    def __init__(self,case_name, expected_result):
        self.case_name = case_name
        self.expected_result = expected_result
        self.actual_result = None

    def run_case(self,user=None,passwd=None):
        print(f"start to run the test case：{self.case_name}. Test data：user name{user},paasword{passwd}===")
        user_info = {"user":"py37", "passwd":"666666"}
        if user == user_info["user"] and passwd == user_info["passwd"]:
            self.actual_result = "success!"
        elif user is None or passwd is None:
            self.actual_result = "user or password missing"
        elif len(user) < 4:
            self.actual_result = "Username length is less than 4"
        elif len(passwd) < 6:
            self.actual_result = "Password length is less than 6"
        elif user != user_info["user"]:
            self.actual_result = "Username is incorrect"
        elif passwd != user_info["passwd"]:
            self.actual_result = "Password is incorrect"
        print(f"The execution is complete. The actual result is：{self.actual_result}")

    def assert_result(self):
        print(f"Compare actual result with expected result. The expected result is：{self.expected_result}")
        if self.actual_result == self.expected_result:
            print("The actual and expected results are the same, success！！")
        else:
            print("Actual and expected results are different，fail！！")

case1 = LoginCase("case1-success","login success")
case1.run_case("py37","666666")
case1.assert_result()

case2 = LoginCase("case2-user_name is incorrect","Username is incorrect")
case2.run_case("py3743","666666")
case2.assert_result()
```
