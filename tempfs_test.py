# -*- coding: UTF-8 -*-
# Copyright 2019 Felix Schwarz
# SPDX-License-Identifier: MIT

from __future__ import absolute_import, print_function, unicode_literals

from pythonic_testcase import *

from fake_fs_helpers import TempFS


class TempFSTest(PythonicTestCase):
    def test_can_create_and_remove_directory(self):
        fs = TempFS.set_up()
        abs_path = fs.create_directory('/foo')
        assert_not_equals('/foo', abs_path)
        assert_path_exists(abs_path)
        fs.rm_tree('/foo')
        assert_path_not_exists(abs_path)
