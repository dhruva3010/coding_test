#overloading
class Calculator:
    def add(self,n1: int, n2: int) -> int:
        return n1 + n2
    
    def add(self, n1: float, n2:float) -> float:
        return n1 + n2

print('Overloading example:')
first_class = Calculator()
print(first_class.add(5,10))
print(first_class.add(7.3, 10.4))

#overriding
class Animal:
    def make_sounds(self):
        print('Some generic sounds')

#inherting Animal class
class Dog(Animal):
    def make_sounds(self):
        print('Bark')

print('Overriding example:')
second_class = Dog()
second_class.make_sounds()