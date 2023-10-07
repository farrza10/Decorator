

/----------multiple Args---------/
def validate_positive_input(func):
    def wrapper(x, y):
        if x <= 0 or y <= 0:
            raise ValueError("Both inputs must be positive")
        return func(x, y)
    return wrapper

@validate_positive_input
def add_positive_numbers(x, y):
    return x + y

result = add_positive_numbers(3, 4)  # This will work.
result = add_positive_numbers(2, -1)  # This will raise a ValueError.



/--------PyFixture-------(run pytest filename.py)----/

import pytest

class MathOperations:
    def add(self, x, y):
        assert x > 0 and y > 0, "Both inputs must be positive"
        return x + y

    def multiply(self, x, y):
        assert x > 0 and y > 0, "Both inputs must be positive"
        return x * y

@pytest.fixture
def math_obj():
    return MathOperations()

def test_add_positive_numbers(math_obj):
    result = math_obj.add(3, 4)
    assert result == 7  # Check if the result is equal to 7

def test_add_negative_number(math_obj):
    with pytest.raises(AssertionError):
        math_obj.add(2, -1)  # This should raise an AssertionError

def test_multiply_positive_numbers(math_obj):
    result = math_obj.multiply(3, 4)
    assert result == 12  # Check if the result is equal to 12

def test_multiply_negative_number(math_obj):
    with pytest.raises(AssertionError):
        math_obj.multiply(2, -1)  # This should raise an AssertionError



/------------AssertMethod--------------/

class MathOperations:
    def add(self, x, y):
        assert x > 0 and y > 0, "Both inputs must be positive"
        return x + y

    def multiply(self, x, y):
        assert x > 0 and y > 0, "Both inputs must be positive"
        return x * y

math_obj = MathOperations()

result = math_obj.add(3, 4)  # This will work.
result = math_obj.add(2, -1)  # This will raise an AssertionError with the specified error message.







/----------Decerator Version----------/
def positive_input(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError("Input must be positive")
        return func(x)
    return wrapper

@positive_input
def square(x):
    return x**2


/--------TraditionalMethod------------/
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
