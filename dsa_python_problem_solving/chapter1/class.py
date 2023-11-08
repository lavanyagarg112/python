def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n

class Fraction:
    def __init__(self, top, bottom):
        if type(top) == int and type(bottom) == int:
            self.num = top
            self.den = bottom
        else:
            raise TypeError("Numerator and denominator must be integers")

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
    
    def __sub__ (self, other_fraction):
        new_num = self.num * other_fraction.den - self.den * other_fraction.num
        new_den = self.den * other_fraction.den
        cmmn = gcd(new_num, new_den)
        return Fraction(new_num//cmmn, new_den//cmmn)
    
    def __truediv__(self, other_fraction):
        if other_fraction.num == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        else:
            new_num = self.num * other_fraction.den
            new_den = self.den * other_fraction.num
            cmmn = gcd(new_num, new_den)
            return Fraction(new_num//cmmn, new_den//cmmn)
        
    def __gt__(self, other_fraction): # greater than
        new_num1 = self.num * other_fraction.den
        new_num2 = other_fraction.den * self.den 
        return new_num1 > new_num2
    
    def __ge__(self, other_fraction): # greater than or equal to
        new_num1 = self.num * other_fraction.den
        new_num2 = other_fraction.den * self.den 
        return new_num1 >= new_num2
    
    def __lt__(self, other_fraction): # less than
        new_num1 = self.num * other_fraction.den
        new_num2 = other_fraction.den * self.den 
        return new_num1 < new_num2
    
    def __le__(self, other_fraction): # less than or equal to
        new_num1 = self.num * other_fraction.den
        new_num2 = other_fraction.den * self.den 
        return new_num1 <= new_num2
    


    def show(self):
        print("{:d}/{:d}".format(self.num, self.den))

x = Fraction(1, 2)
x.show()
y = Fraction(2, -3)
print(y)
print(x*y)
print(x/y)
print(x>y)

z = Fraction(5, 2.0)
z.show()

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


        # super().__init__(lbl), super(UnaryGate, self).__init__(lbl), or super().__init__("UnaryGate", lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0
        
class OrGate(BinaryGate):

    def __init__ (self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a == 1 or b == 1:
            return 1
        else:
            return 0
        
class NotGate(UnaryGate):

    def __init__ (self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin()

        if a == 0:
            return 1
        else:
            return 0
        


#g2 = OrGate("G2")
#print(g2.get_output())

#g3 = NotGate("G3")
#print(g3.get_output())


# Connector
# will not be a part of the gate heirarchy, but is important for making the circuit
# each connector will have two gates on either end
# important in OOP
# we say that a Connector Has-a LogicGate, meaning that connectors will have instances of the LogicGate class within them 
# but are not part of the hierarchy.
# "Has-a-relationship"

# It is very important to distinguish between those that have the Is-a relationship (which requires inheritance) and 
# those that have Has-a relationships (with no inheritance).


# connector: 2 gates, output of one gate becomes input of second gate

#RESUME FROM ANALYSIS OF CODE
class Connector:

    def __init__(self, fgate, tgate): # what really is the function of self?    
        self.from_gate = fgate
        self.to_gate = tgate

    def get_from(self):
        return self.from_gate
    
    def get_to(self):
        return self.to_gate
    
    
    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source

            else:
                raise RuntimeError("Error: NO EMPTY PINS")
            
    '''
    If the input line is not connected to anything (None), then ask the user externally as before. 
    However, if there is a connection, the connection is accessed and from_gate’s output value is retrieved.
    '''

    def get_pin_a(self):
        if self.pin_a == None:
            return input(
                f"Enter pin A input for gate {self.get_label()} : "
            )
        
        else:
            return self.pin_a.get_from().get_output()
        


'''
Create a two new gate classes, one called NorGate the other called NandGate. NandGates work like AndGates that have a 
Not attached to the output. NorGates work lake OrGates that have a Not attached to the output.

Create a series of gates that prove the following equality NOT (( A and B) or (C and D)) is that same as 
NOT( A and B ) and NOT (C and D). Make sure to use some of your new gates in the simulation.
'''

'''
# not working:
class NorGate(BinaryGate):

    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        g1 = OrGate("G1")
        g2 = NotGate("G2")
        return Connector(g1, g2)
    

g1 = NorGate("G1")

'''

'''
# hard code:

class NorGate(BinaryGate):

    def __init__ (self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a != 1 and b != 1:
            return 1
        else:
            return 0
        

class NandGate(BinaryGate):

    def __init__ (self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()

        if a != 1 or b != 1:
            return 1
        else:
            return 0
        
'''

# actual solution

class NandGate(AndGate):

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1
        
class NorGate(OrGate):

    def perform_gate_logic(self):
        if super().perform_gate_logic() == 1:
            return 0
        else:
            return 1



    
#g2 = NandGate("G2")
#print(g2.get_output())



