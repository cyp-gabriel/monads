from bc.monad import monad_checker
from bc.tools import curry2, validator, copy_namedtuple_except, less_than, greater_than
from collections import namedtuple
from pymonad.either import Left, Either

###############################################################################
# XXX
#
is_adult = lambda p: getattr(p, 'age') > 21
is_male = lambda p: getattr(p, 'sex') == 'm'

def increase_age(p, new_age):
    new_p = None
    try:
        new_p = copy_namedtuple_except(Person, p, 'age', 10)
    except Exception as ex:
        new_p = Left("Can't set attribute, fiend.")
    finally:
        return new_p
    

def to_s(p):
    s = f"First name: {getattr(p, 'fname')}"
    s += f"\nLast name: {getattr(p, 'lname')}"
    s += f"\nAge: {getattr(p, 'age')}"
    s += f"\nSex: {getattr(p, 'sex')}"
    return s


###############################################################################
# Entry-point
#
def entry_point():
    try:
        fields = ('fname', 'lname', 'age', 'hotness', 'sex')
        Person = namedtuple("Person", fields, defaults=(None,) * len(fields))
        p = Person('bill', 'esquire', 22, 6, 'm')

        pre = monad_checker(
            validator("Person must be an adult", is_adult),
            validator("Person must be male", is_male))

        post = monad_checker(
            validator("age must be less than 45", lambda p: less_than(45)),
            validator("age must be greater than 10", lambda p: greater_than(10)))

        inc_age = curry2(increase_age)
        
        e = (Either.insert(p)
                .then(pre)
                .then(inc_age(10))
                .then(post)
                .then(to_s))
        print(e)

    except Exception as ex:
        print(ex)


#=================================================>
# -------------
entry_point()