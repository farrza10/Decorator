1.Separation of Concerns:

def validate_positive_input(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive")
        return func(x)
    return wrapper

@validate_positive_input
def square(x):
    return x**2

@validate_positive_input
def calculate_area(radius):
    return 3.14159 * radius**2

# The input validation logic is separated from the core logic of the functions.


2. Reusibility

@validate_positive_input
def cube(x):
    return x**3

# The same 'validate_positive_input' decorator is reused for multiple functions.


3. Decoratio Composition

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@log_function_call
@validate_positive_input
def multiply(a, b):
    return a * b

# The 'multiply' function is decorated with both logging and input validation.









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
