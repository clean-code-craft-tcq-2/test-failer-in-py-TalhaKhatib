
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')

assert(size(38) == 'S') # Input value not catched in conditional statements
print("All is well (maybe!)\n")
