def create_multiplier(n):
    def multiply(x):
        return x*n
    return multiply
double = create_multiplier(2)
triple = create_multiplier(3)
print(double(5))
print(triple(5))
