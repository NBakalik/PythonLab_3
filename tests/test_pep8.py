import os
import unittest
import pycodestyle


class TestPep8(unittest.TestCase):
    def test_pep8(self):
        style = pycodestyle.StyleGuide(quiet=False)
        exclude = set(['venv', 'tests'])
        for root, dirs, files in os.walk('.'):
            dirs[:] = [d for d in dirs if d not in exclude]
            python_files = [os.path.join(root, f) for f in files if f.endswith('.py')]
            style.check_files(python_files)
        n = style.check_files().total_errors

        self.assertEqual(n, 0, 'PEP8 style errors: %d' % n)
