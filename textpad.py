import math
x = -4
if x < 0:
    print("The negative number ", x, " is not valid here.")
    x = 42
    print("I've decided to use the number ", x, " instead.")

print("The square root of ", x, "is", math.sqrt(x))
