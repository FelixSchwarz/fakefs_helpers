# -*- coding: utf-8 -*-
# Copyright (c) 2016-2020 Felix Schwarz
# The source code contained in this file is licensed under the MIT license or
# (at your option) the CC0 v1.0.
# SPDX-License-Identifier: MIT or CC0-1.0

from __future__ import absolute_import, print_function, unicode_literals

import os.path

from .utils import make_string_path


__all__ = ['FakeFS']

_os_path = os.path

class FakeFS(object):
    def __init__(self, patcher):
        self._stubber = patcher
        self._os_path = _os_path

    @classmethod
    def set_up(cls, test=None, **kwargs_patcher):
        global _os_path
        # only require pyfakefs if it is actually used
        from pyfakefs.fake_filesystem_unittest import Patcher
        stubber = Patcher(**kwargs_patcher)
        # keep a reference to the real os.path so we can always use "os.path.isfile()"
        __os_path = os.path
        stubber.setUp()
        _os_path = __os_path
        fake_fs = FakeFS(stubber)
        if test:
            test.addCleanup(fake_fs.tear_down)
        return fake_fs

    def tear_down(self):
        self._stubber.tearDown()

    def __getattr__(self, name):
        if hasattr(self._stubber.fs, name):
            return getattr(self._stubber.fs, name)
        klassname = self.__class__.__name__
        raise AttributeError("AttributeError: %s object has no attribute %r" % (klassname, name))

    def create_file(self, file_path, *args, **kwargs):
        file_path = make_string_path(file_path)
        return self._stubber.fs.create_file(file_path, *args, **kwargs)

    def create_dir(self, directory_path, *args, **kwargs):
        directory_path = make_string_path(directory_path)
        return self._stubber.fs.create_dir(directory_path, *args, **kwargs)
    create_directory = create_dir

    def add_real_file(self, path, *args, **kwargs):
        path_str = make_string_path(path)
        return self._stubber.fs.add_real_file(path_str, *args, **kwargs)

    def add_real_directory(self, path, *args, **kwargs):
        path_str = make_string_path(path)
        return self._stubber.fs.add_real_directory(path_str, *args, **kwargs)

    def add_real_path(self, path, **kwargs):
        path_str = make_string_path(path)
        if self._os_path.isfile(path_str):
            return self.add_real_file(path_str, **kwargs)
        else:
            return self.add_real_directory(path_str, **kwargs)

    def add_real_paths(self, paths, **kwargs):
        for path in paths:
            self.add_real_path(path, **kwargs)

