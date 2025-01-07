from ModuleUser import User

class Admin(User):
    def __init__(self,first_name, last_name, age, blood_group, *privileges):
        super().__init__(first_name,last_name,age,blood_group)
        self.privileges = Privileges(privileges)
    
   
class Privileges:
    def __init__(self, *privileges):
        self.privileges = privileges
    
    def show_privileges(self):
        """Print the user's privileges"""
        print("You have the following privileges:")
        for privilege in self.privileges:
            print(f"-{privilege}")