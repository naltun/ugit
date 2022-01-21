import os
import sys
import unittest

from pathlib import Path
from shutil import rmtree
from subprocess import DEVNULL, STDOUT, check_call
from tempfile import gettempdir

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ugit.data import GIT_DIR


class UgitCore(unittest.TestCase):
    def setUp(self):
        os.chdir(gettempdir())
        if Path(GIT_DIR).is_dir():
            rmtree(GIT_DIR)

    def test_init(self):
        check_call(['ugit', 'init'], stdout=DEVNULL, stderr=STDOUT)
        self.assertTrue(GIT_DIR in os.listdir())


if __name__ == '__main__':
    unittest.main()
