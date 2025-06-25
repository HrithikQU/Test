# multiply_large_numbers.py

def multiply_large_numbers(a: int, b: int) -> int:
    """Multiply two large numbers and return the result."""
    return a * b

if __name__ == "__main__":
    num1 = 123456789012345678901234567890
    num2 = 987654321098765432109876543210
    result = multiply_large_numbers(num1, num2)
    print(f"Multiplication result: {result}")
