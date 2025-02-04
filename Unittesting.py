"""
This module includes a function for checking if a string is a palindrome.

Notes:
    This code was debugged with assistance from OpenAI's ChatGPT, 
    which provided suggestions and support during implementation.

References:
    OpenAI. (2024). ChatGPT (v4.0) [Large language model]. Retrieved from 
    https://openai.com/chatgpt/
"""

import unittest

def is_palindrome(s: str) -> bool:
    """Checks if the given string is a palindrome.

    Args:
        s: The input string to check.

    Returns:
        True if the string is a palindrome, False otherwise.
    """
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned_str == cleaned_str[::-1]


class TestPalindrome(unittest.TestCase):
    """Unit tests for the is_palindrome function."""

    def test_palindrome_true(self):
        """Test that a known palindrome returns True."""
        self.assertTrue(is_palindrome("A man, a plan, a canal, Panama"))

    def test_palindrome_false(self):
        """Test that a non-palindromic string returns False."""
        self.assertFalse(is_palindrome("This sentence is not a palindrome"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
