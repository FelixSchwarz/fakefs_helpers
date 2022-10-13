# -*- coding: utf-8 -*-
# Copyright (c) 2016-2019 Felix Schwarz
# The source code contained in this file is licensed under the MIT license or
# (at your option) the CC0 v1.0.
# SPDX-License-Identifier: MIT or CC0-1.0

from __future__ import absolute_import, print_function, unicode_literals

from collections import namedtuple
import os
import tempfile
import shutil

from .utils import make_string_path


__all__= ['TempFS']

FakeFakeFile = namedtuple('FakeFakeFile', ('name', 'path'))


class TempFS(object):
    def __init__(self, tempdir):
        self.root = tempdir
        # required attribute which is accessed e.g. by FakeFile.__init__()
        self.is_windows_fs = False

    @classmethod
    def set_up(cls, test=None):
        temp_path = tempfile.mkdtemp()
        temp_fs = TempFS(temp_path)
        if test:
            test.addCleanup(temp_fs.tear_down)
        return temp_fs

    def tear_down(self):
        self.rm_tree(self.root)

    def rm_tree(self, path):
        abs_path = self._prefix_with_root_dir(path)
        shutil.rmtree(abs_path)

    def create_directory(self, dirname):
        path = self._prefix_with_root_dir(dirname)
        os.makedirs(path)
        return path

    def create_file(self, path, contents=b''):
        abs_path = self._prefix_with_root_dir(path)
        path_str = make_string_path(path)
        with open(abs_path, 'wb') as fp:
            fp.write(contents)
        return FakeFakeFile(
            name=os.path.basename(path_str),
            path=abs_path,
        )

    def _prefix_with_root_dir(self, path):
        path = make_string_path(path)
        if path.startswith(self.root):
            return path
        if path.startswith(os.sep):
            path = path[len(os.sep):]
        assert not os.path.isabs(path)
        return os.path.join(self.root, path)

