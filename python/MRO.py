# This code demonstrates Python's Method Resolution Order (MRO) in multiple inheritance

class A:
    def method(self):
        print("A method")

class B(A):
    def method(self):
        print("B method")
        super().method()  # Calls the next method in the MRO

class C(A):
    def method(self):
        print("C method")
        super().method()  # Calls the next method in the MRO

class D(B, C):
    pass  # D inherits from both B and C, demonstrating multiple inheritance

# Creating an instance of D
instance_d = D()

# Calling the method on D triggers the MRO
# The order of method calls will be: B -> C -> A
instance_d.method()

# Explanation:
# 1. When instance_d.method() is called, Python looks for the method in class D.
# 2. D doesn't have its own method, so it looks in B (the first parent class).
# 3. B's method is called, printing "B method" and then using super().method().
# 4. super() in B calls C's method (not A's) due to MRO.
# 5. C's method prints "C method" and calls super().method().
# 6. Finally, A's method is called, printing "A method".
# 
# The MRO for class D is: D -> B -> C -> A -> object
# This order ensures a consistent and predictable method resolution in
# complex inheritance hierarchies, avoiding potential ambiguities.
