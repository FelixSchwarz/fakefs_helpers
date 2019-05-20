# -*- coding: utf-8 -*-
# Copyright (c) 2016-2019 Felix Schwarz
# The source code contained in this file is licensed under the MIT license or
# (at your option) the CC0 v1.0.
# SPDX-License-Identifier: MIT or CC0-1.0

from collections import namedtuple
import os
import tempfile
import shutil


__all__ = ['FakeFS', 'TempFS']

class FakeFS(object):
    def __init__(self, patcher):
        self._stubber = patcher

    @classmethod
    def set_up(cls, test=None):
        # only require pyfakefs if it is actually used
        from pyfakefs.fake_filesystem_unittest import Patcher
        stubber = Patcher()
        stubber.setUp()
        fake_fs = FakeFS(stubber)
        if test:
            test.addCleanup(fake_fs.tear_down)
        return fake_fs

    def tear_down(self):
        self._stubber.tearDown()

    def __getattr__(self, name):
        mapping = {
            'create_directory': self._stubber.fs.create_dir,
        }
        if name in mapping:
            return mapping[name]
        if hasattr(self._stubber.fs, name):
            return getattr(self._stubber.fs, name)
        klassname = self.__class__.__name__
        raise AttributeError("AttributeError: %s object has no attribute %r" % (klassname, name))


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
        with open(abs_path, 'wb') as fp:
            fp.write(contents)
        return FakeFakeFile(
            name=os.path.basename(path),
            path=abs_path,
        )

    def _prefix_with_root_dir(self, path):
        if path.startswith(self.root):
            return path
        if path.startswith(os.sep):
            path = path[len(os.sep):]
        assert not os.path.isabs(path)
        return os.path.join(self.root, path)

