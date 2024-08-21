#DECORATORS
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.
def up(text):
    return text.upper()
def low(text):
    return text.lower()
def word(f):
    greet = f("Good Morning !!")
    print(greet)
# word(low)
# word(up)

def greet(function):
    def word():
        print("Good")
        function()
    return word
@greet
def day():
    print("Morning")
@greet
def midday():
    print("Afternoon")
@greet
def night():
    print("Night")


def multiply(a):
    def num(b):
        return a*b
    return num
mul_of_15 = multiply(15)
print(mul_of_15(2))

def division(x):
    def num(y):
        return x/y
    return num
div_of_100 = division(100)
print(div_of_100(2))

