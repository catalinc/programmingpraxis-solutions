#!/usr/bin/env python

# See http://programmingpraxis.com/2011/07/15/json-writing-output/


class Address(object):

    def __init__(self, street, number):
        self.street = street
        self.number = number


class Person(object):

    def __init__(self,
            first_name,
            last_name,
            age,
            gender,
            address):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.address = address


def to_json(obj):
    if obj is None:
        return 'null'
    if isinstance(obj, basestring):
        return "'%s'" % obj
    elif isinstance(obj, (list, tuple)):
        ret = []
        for x in obj:
            ret.append(to_json(x))
        return '[' + ','.join(ret) + ']'
    elif isinstance(obj, dict):
        ret = []
        for k in obj:
            ret.append("'%s': %s" % (k, to_json(obj[k])))
        return '{' + ','.join(ret) + '}'
    else:
        return to_json(getattr(obj, '__dict__', {}))


if __name__ == '__main__':
    address1 = Address('Street A', 1)
    address2 = Address('Street B', 2)
    jim = Person('Jim', 'Jones', 30, 'm', address1)
    jane = Person('Jane', 'Jones', 31, 'f', address2)
    persons = [jim, jane, None]
    print(to_json(persons))
