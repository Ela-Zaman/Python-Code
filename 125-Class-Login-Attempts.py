class User:
    def __init__(self,first_name, last_name, age, blood_group):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.blood_group = blood_group
        self.login_attempts = 0
    
    def describe_user(self):
        print(f"Username: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"blood_group: {self.blood_group}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}\n")
    
    def increment_login_attempts(self):
        self.login_attempts+=1

    def reset_login_attempt(self):
        self.login_attempts = 0
ela= User("Razia Zaman", "Ela", 27, "B+")
ela.increment_login_attempts()
ela.increment_login_attempts()
ela.increment_login_attempts()
ela.increment_login_attempts()
print(f"The No. of login Attempts {ela.login_attempts} ")
ela.reset_login_attempt()
print(f"After resetting the no. of login attempts {ela.login_attempts} ")