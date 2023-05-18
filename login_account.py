# Acount class for a customer to either signUp or LogIn into mama 
# Mboga's online Grocery web App

class Account:
    def __init__(self,name, password):
        self.name = name
        self.password = password

def login(self,name, password):
    name=input("Enter your name:")
    password=input("Enter your password:")
    password=input("Confirm your password:")
    if self.name ==name and self.password == password:
        return "Login successful"
    else:
        return "Invalid name or password"

def signup(self, name, password,confirm_password):
    name=input("Enter your name:")
    password=input("Enter your password:")
    self.name = name
    self.password = password
    self.confirm_password=confirm_password
    return "Signup successful"
account1=Account("cynthia",123456)
print(login(self=login,name="cynthia",password=6798))

account2=Account("mumbua",89087)
print(signup(self=signup,name="mumbua",password=6899))
print(signup(self=signup,name="mumbua",confirm_password=6899))