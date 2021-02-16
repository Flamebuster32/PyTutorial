# we can actually call other functions within a function
# heck we can call functions within themselves these are called recursive functions


def pront(a):  # we create a function pront with argument a
    print(a)  # we print a
    pront(a)  # we call the function pront with value a


pront("loop?")  # we call the function pront with value 'loop?'
# see the problem with this is theirs a maximum recursion loop within python, in most actual code it doesnt matter
# but in the example we gave below we just repeatedly print 'loop?' until we reach the recursion limit and get an
# error
