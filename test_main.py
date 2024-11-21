import pytest

from main import count_vowels

def test_all_vowels():
    assert count_vowels("aeiou") == 5

def test_no_vowels():
    assert count_vowels("bcdfg") == 0

def test_mixed_vowels():
    assert count_vowels("Hello World!") == 3
