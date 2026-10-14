class RectLike:

    def __init__(self, w, h):
        self.width = w
        self.height = h

class MyClass:
        
    def __init__(self):
        self._w = 900
        self._h = 600

    def get_rect(self):
        return RectLike(self._w, self._h)

my_object = MyClass()
print(my_object.get_rect().width)
