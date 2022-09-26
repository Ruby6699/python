# Define a login test case named class LoginCase.
# Each instance is a login test case.
# attribute:case_name, expected_result,actual_result
# Method 1: Run the test case
# Description: There are 2 parameters: username and password.
# That can log in successfully: Username: py37, password: 666666.
# Instruction: whether the login is successful by whether the user name and password are correct or not. Return the actual result.
# ps: Non-compliance can be considered: password length is not 6 digits/password incorrect/username is incorrect.
# Method 2: Compare the expected_result and the actual result.
# Instantiate 2 test cases, and run the instance (call the method), render the method (call the result)

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

