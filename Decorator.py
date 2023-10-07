
-----Decerator Version------
def positive_input(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive")
        return func(x)
    return wrapper

@positive_input
def square(x):
    return x**2


----TraditionalMethod----
def square(x):
    if x <= 0:
        raise ValueError("Input must be positive")
    return x**2

# Now, calling the square function will perform input validation.
try:
    result = square(-5)
except ValueError as e:
    print(e)  # This will print: "Input must be positive"
else:
    print(result)
