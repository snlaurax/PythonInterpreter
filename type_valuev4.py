import copy

from enum import Enum
from intbase import InterpreterBase


# Enumerated type for our different language data types
class Type(Enum):
    INT = 1
    BOOL = 2
    STRING = 3
    CLOSURE = 4
    NIL = 5
    OBJECT = 6

class Object:
    def __init__(self):
        self.fields = {}

    def update(self, key, source):
        self.fields[key] = source
    
    def get (self, key):
        if key in self.fields:
            return self.fields[key]
        elif "proto" in self.fields and self.fields["proto"].v:
            return self.fields["proto"].v.get(key)


class Closure:
    def __init__(self, func_ast, env):
        # self.captured_env = copy.deepcopy(env) 
        self.captured_env = []
        for value in env.environment:
            if  bool(value):
                new_dict = {}
                for key, value_obj in value.items():
                    if value_obj.t == Type.OBJECT:
                        new_dict[key] = value_obj
                    else:
                        new_dict[key] = copy.deepcopy(value_obj)
                self.captured_env.append(new_dict)
        self.func_ast = func_ast
        self.type = Type.CLOSURE

# Represents a value, which has a type and its value
class Value:
    def __init__(self, t, v=None):
        self.t = t
        self.v = v

    def value(self):
        return self.v

    def type(self):
        return self.t

    def set(self, other):
        self.t = other.t
        self.v = other.v


def create_value(val):
    if val == InterpreterBase.TRUE_DEF:
        return Value(Type.BOOL, True)
    elif val == InterpreterBase.FALSE_DEF:
        return Value(Type.BOOL, False)
    elif isinstance(val, str):
        return Value(Type.STRING, val)
    elif isinstance(val, int):
        return Value(Type.INT, val)
    elif val == InterpreterBase.NIL_DEF:
        return Value(Type.NIL, None)
    else:
        raise ValueError("Unknown value type")


def get_printable(val):
    if val.type() == Type.INT:
        return str(val.value())
    if val.type() == Type.STRING:
        return val.value()
    if val.type() == Type.BOOL:
        if val.value() is True:
            return "true"
        return "false"
    return None
