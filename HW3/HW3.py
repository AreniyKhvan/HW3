import string

def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())  # ������� ������� � ����� ����������
    return "Yes" if cleaned == cleaned[::-1] else "No"

# �������
print(is_palindrome("Turan"))  # No
print(is_palindrome("A man, a plan, a canal, Panama"))  # Yes

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# �������
print(factorial(3))  # 6
print(factorial(5))  # 120

def smallest_divisor(x):
    for i in range(2, x + 1):
        if x % i == 0:
            return i

# �������
print(smallest_divisor(6))  # 2