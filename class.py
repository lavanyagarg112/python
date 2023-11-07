def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return "{:d}/{:d}".format(self.num, self.den)

    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num

    def __add__(self, other_fraction):
        new_num = self.num * other_fraction.den \
        + self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num // cmmn, new_den // cmmn)
    
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den) # return in shortest form
        return Fraction(new_num // cmmn, new_den // cmmn)


    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

x = Fraction(1, 2)
x.show()
y = Fraction(2, 3)
print(y)
print(x + y)
print(x == y)
print(x*y)

'''
To enable the use of operators with instances of a custom class, you need to implement the corresponding special methods 
(also known as magic methods) with the exact names that Python expects. 

Here are some of the most common ones related to arithmetic and comparison operations:

- `__add__(self, other)`: for addition `+`
- `__sub__(self, other)`: for subtraction `-`
- `__mul__(self, other)`: for multiplication `*`
- `__truediv__(self, other)`: for division `/`
- `__floordiv__(self, other)`: for floor division `//`
- `__mod__(self, other)`: for modulo `%`
- `__pow__(self, other[, modulo])`: for power `**`
- `__lt__(self, other)`: for less than `<`
- `__le__(self, other)`: for less than or equal `<=`
- `__eq__(self, other)`: for equality `==`
- `__ne__(self, other)`: for inequality `!=`
- `__gt__(self, other)`: for greater than `>`
- `__ge__(self, other)`: for greater than or equal `>=`

These methods allow you to define how instances of your class should behave when used with the corresponding operators. 
If you do not implement the relevant method for an operator, trying to use that operator with instances of your class will 
raise a `TypeError`.
'''

'''
Inheritance in object orientation programming

1) An inheritance heirarchy for Python Collections

Sequential collections and Non sequential Collection

Lists, tuples, and strings are all examples of sequential collections. They all inherit common data organization and operations. 
However, each of them is distinct based on whether the data is homogeneous and whether the collection is immutable. 
The children all gain from their parents but distinguish themselves by adding additional characteristics.

Similarly Non sequential collection includes dictionary and sets


2) An inheritance heirarchy for Logic gates
Binary gate (And, or) and Unary gate (not)


'''

# implementing inheritance

class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()  # based on the type of gate - powerful concept in OOP, writng method we dont know implementation of
        return self.output
    

class BinaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        return int(input(f"Enter pin A input for gate \
            {self.get_label()}: "))

    def get_pin_b(self):
        return int(input(f"Enter pin B input for gate \
            {self.get_label()}: "))
    
class UnaryGate(LogicGate):        
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        self.pin = None

    def get_pin(self):
        return int(input(f"Enter pin input for gate \
            {self.get_label()}: "))
    
class AndGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl) # Super used in place of explicitly naming parent class
        # used when a class has more than one parent
        # we pass binary gate -> another class and thus this is the parent class
        # when we pass another class in the parenthesis
        # the class is the superclass
        # and the new class is the subclass

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        



