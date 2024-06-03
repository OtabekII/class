class MyClass:
    def __init__(self):
        self.data = []
        self.original_data = []

    def append(self, item):
        self.data.append(item)
        self.original_data = self.data.copy()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None:
            self.data = self.original_data.copy()
        return exc_type is None

    def __str__(self):
        return f"MyClass(data={self.data})"

with MyClass() as obj:
    obj.append(1)
    obj.append(2)
    obj.append(3)
    raise ValueError("Xatolik ro'y berdi")

print(obj)  