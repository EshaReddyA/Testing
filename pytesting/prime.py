import pytest

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def test_prime_numbers():
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True

def test_non_prime_numbers():
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(4) is False
    assert is_prime(-3) is False
