import unittest
# Assuming src/main.py is in the same directory as test.py for simplicity.
# If src/main.py is in a parent directory or elsewhere,
# you might need to adjust the import path (e.g., from ..src.main import receivedText)
# or add src/main.py's directory to sys.path.
from src.main import receivedText # This assumes src/main.py exists and receivedText is defined there

class TestReceivedText(unittest.TestCase):

    def test_sample_case_0(self):
        """Tests the given sample case."""
        input_string = "HE*<LL>O"
        expected_output = "LLHO"
        self.assertEqual(receivedText(input_string), expected_output)

    def test_empty_string(self):
        """Tests with an empty input string."""
        input_string = ""
        expected_output = ""
        self.assertEqual(receivedText(input_string), expected_output)

    def test_backspace_on_empty(self):
        """Tests backspace when text is empty."""
        input_string = "*"
        expected_output = ""
        self.assertEqual(receivedText(input_string), expected_output)

    def test_numeric_lock_toggle(self):
        """Tests numeric lock turning numbers on and off."""
        input_string = "123#456#789"
        expected_output = "123789" # 456 should be ignored
        self.assertEqual(receivedText(input_string), expected_output)

    def test_home_key_insertion(self):
        """Tests insertion after Home key."""
        input_string = "ABC<DEF"
        expected_output = "DEFABC"
        self.assertEqual(receivedText(input_string), expected_output)

    def test_end_key_insertion(self):
        """Tests insertion after End key."""
        input_string = "ABC<DE>FG"
        expected_output = "DEABC FG" # DE typed at start, cursor moves to end, FG typed at end
        self.assertEqual(receivedText(input_string), expected_output.replace(" ", "")) # Remove space for actual check

    def test_complex_sequence(self):
        """Tests a more complex sequence of operations."""
        input_string = "Hello_World!*<Python is >great!"
        # Initial: Hello_World!
        # *: Hello_World
        # <: |Hello_World
        # Python is : Python is Hello_World
        # >: Python is Hello_World|
        # great!: Python is Hello_Worldgreat!
        expected_output = "Python is Hello_Worldgreat!"
        self.assertEqual(receivedText(input_string), expected_output)

    def test_numeric_lock_off_initially(self):
        """
        Tests behavior if numeric lock was off initially (though problem states it's on).
        This is for exploring problem variations or double-checking constraints.
        For *this* problem, initial numeric lock is ON.
        """
        # This test case would require modifying the function if initial state changes.
        # As per problem, initial numeric_lock_on = True.
        # This test is more for demonstrating flexibility.
        pass

    def test_multiple_home_end(self):
        """Tests repeated Home/End presses."""
        input_string = "ABC<DEF<GHI>JKL>MNO"
        # ABC -> ABC
        # <DEF -> DEFABC
        # <GHI -> GHIDEFABC
        # >JKL -> GHIDEFABCJKL
        # >MNO -> GHIDEFABCJKLMNO
        expected_output = "GHIDEFABCJKLMNO"
        self.assertEqual(receivedText(input_string), expected_output)

# This block allows running tests directly from this file
if __name__ == '__main__':
    unittest.main()