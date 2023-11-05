from GlitchPrompts import glitch_print
import unittest
import io
import sys


class GlitchPrintTests(unittest.TestCase):
    def test_type_error(self):
        with self.assertRaises(TypeError):
            glitch_print("Success", prompt="bad_prompt_type")
