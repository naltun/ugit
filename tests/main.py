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
        self.object_id = None
        self.tmp_path = gettempdir()
        self.objects_path = f'{self.tmp_path}/{GIT_DIR}/objects'

        os.chdir(self.tmp_path)
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
        self._test_cat_file()

    def _test_init(self):
        run(['ugit', 'init'], stdout=DEVNULL, stderr=STDOUT)
        self.assertTrue(GIT_DIR in os.listdir())

    def _test_hash_object(self):
        tmp = NamedTemporaryFile()
        with open(tmp.name, 'w') as f:
            body = 'Hello, World!'
            f.write(body)
        resp = run(['ugit', 'hash-object', tmp.name], capture_output=True).stdout
        # e.g. resp == b'0a0a9f2a6772942557ab5355d76af442f8f65e01\n', so let's decode and remove the
        # newline character.
        self.object_id = resp.decode().rstrip()
        self.assertTrue(
            self.object_id in os.listdir(f'{gettempdir()}/{GIT_DIR}/objects')
        )

    def _test_cat_file(self):
        body = 'Hello, World!'
        # e.g. resp == b'Hello, World!', so we must decode it.
        resp = run(
            ['ugit', 'cat-file', self.object_id], capture_output=True
        ).stdout.decode()
        self.assertTrue(body == resp)


if __name__ == '__main__':
    unittest.main()
