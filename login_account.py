class Account:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    def signup(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")

        if password == confirm_password:
            self.name = name
            self.password = password
            return "Signup successful"
        else:
            return "Password confirmation failed"

    def login(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")

        if self.name == name and self.password == password:
            return "Login successful"
        else:
            return "Invalid name or password"


account1 = Account("mumbua", 89087)
print(account1.signup())

account2 = Account("cynthia", 123456)
print(account2.login())
