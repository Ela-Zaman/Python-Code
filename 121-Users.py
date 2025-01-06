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

ela= User("Razia Zaman", "Ela", 27, "B+")
ela.describe_user()
ela.greet_user()
doha= User("Doha","Ahmed", 23, "B+")
doha.describe_user()
doha.greet_user()
toha= User("Toha", "Ahmed", 18, "B+")
toha.describe_user()
toha.greet_user()
