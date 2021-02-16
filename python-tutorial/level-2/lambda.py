# lambda is a function that takes any number of arguments but only 1 expression
x = lambda a: a * 2
print(x(10))


# you might be asking, why not just use functions?
# lambda is actually very powerful when used as an anonymous function within another function
def fun(n):
    return lambda a: a * n


dub = fun(2)
tri = fun(3)
quad = fun(4)
print(dub(8), "\n", tri(3), "\n", quad(10))  # \n is used for newline
