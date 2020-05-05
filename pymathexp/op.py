from inspect import signature

import math

class Op():
    def __init__(self, name, function, precedence=-1, associativity=0):
        self.name = name
        self.function = function
        self.num_of_operands = len(signature(function).parameters)
        self.precedence = precedence
        self.associativity = associativity

def factorial(n: int):
    return n*factorial(n-1) if n > 0 else 1

operations = {
    "+": Op("+", lambda a, b: a+b, 0, 0),
    "-": Op("-", lambda a, b: a-b, 0, 0),
    "*": Op("*", lambda a, b: a*b, 1, 0),
    "/": Op("/", lambda a, b: a/b, 1, 0),
    "^": Op("^", lambda a, b: a**b, 2, 1),
    "sin": Op("sin", lambda a: math.sin(a)),
    "cos": Op("cos", lambda a: math.cos(a)),
    "tan": Op("tan", lambda a: math.tan(a)),
    "asin": Op("asin", lambda a: math.asin(a)),
    "acos": Op("acos", lambda a: math.acos(a)),
    "atan": Op("atan", lambda a: math.atan(a)),
    "!": Op("!", lambda a: factorial(a)),
    "C": Op("C", lambda a, b: factorial(a)/(factorial(a-b)*factorial(b))),
    "P": Op("P", lambda a, b: factorial(a)/factorial(a-b))
}

def update_op(name=None, function=None, precedence=-1, associativity=0, dict=None, to_append=operations):
    to_append.update({name: Op(name, function, precedence, associativity)})