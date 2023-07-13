

class A:
    def __init__(self, a, b, c):  # init method is used to pass value as parameterized constructor
        self.__a = a
        self._b = b
        self.c = c
    
    def display(self):
        print("Values of a, b and c are:")
        print(f"a={self.__a}, b={self._b}, c={self.c}")

class B(A):
    def display(self):
        try:
            print("Value of a=", self.__a)
        except AttributeError:
            print("private variable cannot be accessed from a different class")
        finally:
            print("values are:")
            print(f"b={self._b}\nc={self.c}")

obj = B(30,70,90)
obj.display()
