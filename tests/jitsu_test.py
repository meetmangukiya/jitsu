import os
import shutil
import textwrap
import unittest

from test.support import captured_stdout

from jitsu.__main__ import main


class TestJitsu(unittest.TestCase):
    def setUp(self):
        os.chdir(os.path.join(os.path.dirname(__file__), 'jitsu-test'))

    def tearDown(self):
        shutil.rmtree('_dist')

    def test_generate(self):
        main([])

        with open('_dist/life.txt') as f:
            expected = textwrap.dedent("""
            Life?

            Life
            is
            Mystery


            ~ Meet Mangukiya
            """)[1:-1]

            self.assertEqual(f.read(), expected)
