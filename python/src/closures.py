#!/usr/bin/python

# Python implementation of 
# http://www.skorks.com/2010/05/closures-a-simple-explanation-using-ruby/

class SomeClass(object):

    def __init__(self, value):
        self.value = value

    @property
    def value_printer(self):
        def closure():
            print("value: %s" % self.value)
        return closure

    @property
    def value_incrementer(self):
        def closure():
            self.value += 1
        return closure

o = SomeClass(2)

printer = o.value_printer
incrementer = o.value_incrementer

for _ in xrange(3):
    incrementer()
    printer()
