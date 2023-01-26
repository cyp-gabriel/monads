# v1.0

## main2.py

Demonstrates validator, checker, monad_checker--all work in conjunction with pymonad.  Here is the interesting code:

```python
# Set up input: Person object
fields = ('fname', 'lname', 'age', 'hotness', 'sex')
Person = namedtuple("Person", fields, defaults=(None,) * len(fields))
p = Person('bill', 'esquire', 22, 6, 'm')

# set up pre- and post-conditions
pre = monad_checker(
   validator("Person must be an adult", is_adult),
   validator("Person must be male", is_male))

post = monad_checker(
   validator("age must be less than 45", lambda p: less_than(45)),
   validator("age must be greater than 10", lambda p: greater_than(10)))

# this is the processing step
inc_age = curry2(increase_age)

# set up chain
e = (Either.insert(p)
       .then(pre)
       .then(inc_age(10))
       .then(post)
       .then(to_s))
print(e)

```
