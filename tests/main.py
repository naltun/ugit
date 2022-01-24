import logging
import os
import random
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
        self.file_body = f'Random Bytes: {random.randbytes(10_000)}'
        self.object_id = None
        self.tmp_path = gettempdir()
        self.objects_path = f'{self.tmp_path}/{GIT_DIR}/objects'
        self.test_count = 0

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

    def _increment_test_count(self):
        self.test_count += 1
        return self.test_count

    def _test_init(self):
        logging.debug(f'{self._increment_test_count()} Running sub-test:')

        run(['ugit', 'init'], stdout=DEVNULL, stderr=STDOUT)
        self.assertTrue(GIT_DIR in os.listdir())

    def _test_hash_object(self):
        logging.debug(f'{self._increment_test_count()} Running sub-test:')

        tmp = NamedTemporaryFile()
        with open(tmp.name, 'w') as f:
            f.write(self.file_body)
        resp = run(['ugit', 'hash-object', tmp.name], capture_output=True).stdout
        # resp will be a bytestring and end in a newline character, so let's decode the value and
        # remove the trailing newline.
        self.object_id = resp.decode().rstrip()
        self.assertTrue(
            self.object_id in os.listdir(f'{self.tmp_path}/{GIT_DIR}/objects')
        )

    def _test_cat_file(self):
        logging.debug(f'{self._increment_test_count()} Running sub-test:')

        # resp will be a bytestring, so we must decode it.
        resp = run(
            ['ugit', 'cat-file', self.object_id], capture_output=True
        ).stdout.decode()
        self.assertTrue(self.file_body == resp)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG, format='%(message)s %(funcName)s')
    unittest.main()
