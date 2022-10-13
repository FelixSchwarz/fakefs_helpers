# -*- coding: utf-8 -*-
# The source code contained in this file is licensed under the MIT license or
# (at your option) the CC0 v1.0.
# SPDX-License-Identifier: MIT or CC0-1.0

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path
from unittest import TestCase

from schwarz.fakefs_helpers import FakeFS


class FakeFSTest(TestCase):
    def setUp(self):
        self.fs = FakeFS.set_up(test=self)

    def test_can_create_file(self):
        self.fs.create_file('/foo.txt', contents=b'secret')
        with open('/foo.txt', 'rb') as fp:
            file_content = fp.read()
        assert (file_content == b'secret')

    def test_create_file_with_path_instance(self):
        path = Path('/foo.txt')
        fake_file = self.fs.create_file(path, contents=b'secret')
        with open(fake_file.path, 'rb') as fp:
            file_content = fp.read()
        assert (file_content == b'secret')

    def test_add_real_file(self):
        this_file = __file__
        try:
            open(this_file, 'r')
        except IOError:
            # file not present in the virtual file syste
            pass

        self.fs.add_real_file(this_file)
        with open(this_file, 'r') as fp:
            assert 'SPDX-License-Identifier' in fp.read()

    def test_add_real_directory(self):
        this_dir = Path(__file__).parent
        assert not this_dir.exists()

        self.fs.add_real_directory(this_dir)
        assert this_dir.is_dir()

    def test_create_directory_with_path_instance(self):
        path = Path('/foo')
        fake_dir = self.fs.create_directory(path)
        assert Path(fake_dir.path).is_dir()

