class User:
    def __init__(self,first_name, last_name, age, blood_group):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.blood_group = blood_group
    
    def describe_user(self):
        print(f"Username: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"blood_group: {self.blood_group}")

    def greet_user(self):
        print(f"Welcome {self.first_name} {self.last_name}\n")