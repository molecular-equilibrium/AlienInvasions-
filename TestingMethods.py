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
# NO wayy!!!
# Here we we have two classes, RectLike and MyClass.
# This program is demonstrating how one class uses
# a method that returns an object from another class.
# In this case, the RectLike class. In the MyClass
# class, it has two methods - the init method and the 
# get_rect method. The init method eststablishes attributes
# that will be used later on, the get_rect method returns an object
# from the RectLike class, and is passed the aruments self._w and
# self._h that were established in the init method.
# On line 16, we create an instance of the object that is
# stored in the variable called my_object.
# we use the print() function to display the results.
# Inside it is my_object.get_rect().width. 
# The print call then has the get_rect method return
# object which then allows us to access that objects attributes.
# This is what is happening in pygame, you use methods and classes
# like this and it is a extremely powerful way to write code.