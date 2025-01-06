class Dog:
    """A Simple attempt to model a dog."""

    def __init__(self,name,age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over !")

my_dog = Dog("Willie", 6)

print(f"My dog's name is {my_dog.name}")
print(f"The age of my dog is {my_dog.age}")

my_dog.sit()
my_dog.roll_over()

your_dog= Dog("Lucie", 4)
print(f"Your dog is {your_dog.name} and it is {your_dog.age} years old")
your_dog.roll_over()