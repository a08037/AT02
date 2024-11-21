def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

def test_empty_string():
    assert count_vowels("") == 0
