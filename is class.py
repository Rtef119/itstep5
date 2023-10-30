class First_class:
    pass

class Second_class(First_class):
    pass

obj = Second_class() #obj = Second_class

print(isinstance(obj,Second_class))#print(issubclass(First_class,Second_class))
print(isinstance(obj,First_class))#print(issubclass(Second_class,First_class))