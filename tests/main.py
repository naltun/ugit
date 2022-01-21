import os
import sys
import unittest

from pathlib import Path
from shutil import rmtree
from subprocess import DEVNULL, STDOUT, run
from tempfile import NamedTemporaryFile, gettempdir

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from ugit.data import GIT_DIR


class UgitCore(unittest.TestCase):
    def setUp(self):
        os.chdir(gettempdir())
        if Path(GIT_DIR).is_dir():
            rmtree(GIT_DIR)

    def test_ugit(self):
        '''
        Test suite entrypoint. `unittest' will not run tests sequentially, which is required. `ugit init'
        must come before any of the other sub-commands, so this single unit test is composed of various
        sub-tests.
        '''
        self._test_init()
        self._test_hash_object()

    def _test_init(self):
        run(['ugit', 'init'], stdout=DEVNULL, stderr=STDOUT)
        self.assertTrue(GIT_DIR in os.listdir())

    def _test_hash_object(self):
        tmp = NamedTemporaryFile()
        with open(tmp.name, 'w') as f:
            body = 'Hello, World!'
            f.write(body)
        obj_id = run(['ugit', 'hash-object', tmp.name], capture_output=True)
        # e.g. obj_id == b'0a0a9f2a6772942557ab5355d76af442f8f65e01\n'
        self.assertTrue(obj_id.stdout.decode().rstrip() in os.listdir(f'{gettempdir()}/{GIT_DIR}/objects'))


if __name__ == '__main__':
    unittest.main()
