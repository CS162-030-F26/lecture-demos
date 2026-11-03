# A class can inherit attributes from another class.

# In this context, the class doing the inheriting is referred to as the
# derived class, AKA the child class, AKA the subclass

# The class that is being inherited from is referred to as the base class,
# AKA the parent class, AKA the superclass.

# When you create an inheritance relationship, every attribute that is defined
# in the base class becomes implicitly also defined in the derived class.

from dog import Dog

# The Husky class is derived from the Dog class (the Husky class inherits from
# the Dog class).
class Husky(Dog):
    pass
