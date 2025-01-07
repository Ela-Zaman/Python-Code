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

class Admin(User):
    def __init__(self,first_name, last_name, age, blood_group, *privileges):
        super().__init__(first_name,last_name,age,blood_group)
        self.privileges = privileges
    
    def show_privileges(self):
        print("You have the following privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")

ela= Admin("Razia Zaman", "Ela", 23, "B+","Can Login","Can Order","Can pay", "Visualize Market Share")

ela.show_privileges()
