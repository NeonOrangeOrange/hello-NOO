
from . import greetings as _greetings

def greet_with_name(greeting, name):
    print(greeting +',', name+'!')


if __name__ == "__main__":
    greet_with_name("Welcome", "Python")
    greet_with_name(_greetings.hi(), "Python")
