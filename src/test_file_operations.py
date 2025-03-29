import os
from file_operations import cpy_src_to_dst
from pathlib import Path
import unittest

class TestFileOperations(unittest.TestCase):
    def test_src_does_not_exist(self):
        with self.assertRaises(ValueError):
            cpy_src_to_dst(Path("asdfjkl"), Path("new_dst"))
