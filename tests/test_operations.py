import pytest
from app.operation import Operation

# -----------------------------------------------------------------------------------
# Test Addition Method
# -----------------------------------------------------------------------------------

def test_addition_positive():
    """
        Test the addition method with two positive numbers.

        verfies that addition two positive number returns correct sum.
    """

    a = 5.0
    b = 2.0
    expected = 7.0

    result = Operation.addition(a,b)

    assert result == expected, f"expected {a} + {b} to be {expected}, got {result}"


def test_addition_negative():
    """
        test the addition method with two negative numbers
        
        verify adding two negative numbers returns correct sum 
    """

    a = -1.0
    b = -3.0
    expected = -4.0

    result = Operation.addition(a,b)

    assert result == expected, f"expected {a} + {b} to be {expected}, got {result}"

def test_addition_positive_negative():
    """
        test the addition method with positive and negative numbers
        
        verify adding two negative numbers returns correct sum 
    """

    a = 3.0
    b = -1.0
    expected = 2.0

    result = Operation.addition(a,b)

    assert result == expected, f"expected {a} + {b} to be {expected}, got {result}"

def test_addition_with_0():
    """
        test the addition method with zero as one of operands
        
        verify adding zero to a number returns number itself.
    """

    a = 5.0
    b = 0.0
    expected = 5.0

    result = Operation.addition(a,b)

    assert result == expected, f"expected {a} + {b} to be {expected}, got {result}"

# -----------------------------------------------------------------------------------
# Test Subtraction Method
# -----------------------------------------------------------------------------------

def test_subtraction_positive():
    """
        test the subtraction method with two positive operands

        verify subtracting one positive number from another returns corrent difference
    """

    a = 5.0
    b = 1.0
    expected = 4.0

    result = Operation.subtraction(a,b)

    assert result == expected, f"expected {a} - {b} to be {expected}, got {result}"

def test_subtraction_negative():
    """
        test the subtraction method with two negative operands

        verify subtracting one negative number from another returns corrent difference
    """

    a = -5.0
    b = -1.0
    expected = -4.0

    result = Operation.subtraction(a,b)

    assert result == expected, f"expected {a} - {b} to be {expected}, got {result}"

def test_subtraction_positive_negative():
    """
        test the subtraction method with one positive and one negative operand

        verify subtracting one negative number from a positive number returns corrent difference
    """
    a = 5.0
    b = -1.0
    expected = 6.0

    result = Operation.subtraction(a,b)

    assert result == expected, f"expected {a} - {b} to be {expected}, got {result}"

def test_subtraction_with_zero():
    """
        test the subtraction method with zero as one of operands

        verify subtracting zero from a number returns number itself
    """
    a = 5.0
    b = -1.0
    expected = 6.0

    result = Operation.subtraction(a,b)

    assert result == expected, f"expected {a} - {b} to be {expected}, got {result}"

# -----------------------------------------------------------------------------------
# Test Multiplication Method
# -----------------------------------------------------------------------------------

def test_multiplication_positive():
    """
        Test multiplication method with two positive operands

        verify multiplying two positive numbers returns correct product
    """

    a = 2.0
    b = 5.0
    expected = 10.0

    result = Operation.multiplication(a,b)

    assert result == expected, f"expected {a} * {b} to be {expected}, got {result}"

def test_multiplicaiton_negative():
    """
        Test multiplication method with two negative operands

        verify multiplying two negative numbers returns correct product
    """

    a = -2.0
    b = -5.0
    expected = 10.0

    result = Operation.multiplication(a,b)

    assert result == expected, f"expected {a} * {b} to be {expected}, got {result}"

def test_multiplicaiton_positive_negative():
    """
    Test multiplication method with a positive and negative operand

    verify multiplying a negative number and a positive number returns correct product
    """

    a = 2.0
    b = -5.0
    expected = -10.0

    result = Operation.multiplication(a,b)

    assert result == expected, f"expected {a} * {b} to be {expected}, got {result}"

def test_multiplication_with_zero():
    """
    Test multiplication method with zero as an operans 

    verify multiplying a negative number and a positive number returns correct product

    """

    a = 0.0
    b = 10.0
    expected = 0.0

    result = Operation.multiplication(a,b)

    assert result == expected, f"expected {a} * {b} to be {expected}, got {result}"

# -----------------------------------------------------------------------------------
# Test Division Method
# -----------------------------------------------------------------------------------

def test_division_positive():
    """
    Test the division method with two positive numbers.
    
    verifiy that dividing two positive numbers returns the correct quotient.
    """
    a = 10.0
    b = 5.0
    expected_result = 2.0

    result = Operation.division(a,b)

    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_negative_numbers():
    """
    Test the division method with two negative numbers.
    
    verify that dividing two negative numbers returns the correct quotient.
    """

    a = -10.0
    b = -5.0
    expected_result = 2.0

    result = Operation.division(a,b)

    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"


def test_division_positive_negative():
    """
    Test the division method with one positive and one negative number.
    
    verify that dividing a positive number by a negative number returns the correct quotient.
    """

    a = 10.0
    b = -5.0
    expected_result = -2.0

    result = Operation.division(a,b)

    assert result == expected_result, f"Expected {a} / ({b}) to be {expected_result}, got {result}"


def test_division_with_zero_divisor():
    """
    Test the division method with zero as the divisor.
    
    verify that dividing any number by zero raises a ValueError.
    """

    a = 10.0
    b = 0.0

    with pytest.raises(ValueError) as exc_info:
        Operation.division(a,b)
    
    assert str(exc_info.value) == "cannot divide by 0"


def test_division_with_zero_numerator():
    """
    Test the division method with zero as the numerator.
    
    verify that dividing zero by a non-zero number returns zero.
    """

    a = 0.0
    b = 5.0
    expected_result = 0.0

    result = Operation.division(a,b)

    assert result == expected_result, f"Expected {a} / {b} to be {expected_result}, got {result}"

# -----------------------------------------------------------------------------------
# Test Invalid Input Types (Negative Testing)
# -----------------------------------------------------------------------------------

@pytest.mark.parametrize("calc_method, a, b, expected_exception", [
    (Operation.addition, '10', 5.0, TypeError),
    (Operation.subtraction, 10.0, '5', TypeError),
    (Operation.multiplication, '10', '5', TypeError),
    (Operation.division, 10.0, '5', TypeError),
])
def test_operations_invalid_input_types(calc_method, a, b, expected_exception):
    """
    Test that arithmetic methods raise TypeError when provided with invalid input types.
    
    verifify that providing non-float inputs to the arithmetic methods raises
    a TypeError, as the operations are intended for floating-point numbers.
    """

    with pytest.raises(expected_exception):
        calc_method(a,b)
    