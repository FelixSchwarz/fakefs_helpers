# -*- coding: utf-8 -*-
# The source code contained in this file is licensed under the MIT license or
# (at your option) the CC0 v1.0.
# SPDX-License-Identifier: MIT or CC0-1.0

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

