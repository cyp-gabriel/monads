from bc.tools import curry1, curry2, retarg

_identity = curry1(retarg)

less_than = curry2(lambda lhs, rhs: lhs < rhs)
greater_than = curry2(lambda lhs, rhs: lhs > rhs)
