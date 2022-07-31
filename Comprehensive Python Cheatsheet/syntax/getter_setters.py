class MyClass:
    @property
    def a(self):
        return self._a
    @a.setter
    def a(self, value):
        self._a = value

obj = MyClass
obj.a = 123
print(obj.a)
