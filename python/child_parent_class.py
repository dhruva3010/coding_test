class Parent:
    def __init__(self, name):
        self.name = name

    def show_info(self):
        print(f"Name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show_info(self):
        super().show_info()
        print(f"Age: {self.age}")

# Creating an instance of the Child class
child_instance = Child("John", 25)

# Calling the overridden method in Child, which also calls the method in Parent using super()
child_instance.show_info()
