# -*- coding: utf-8 -*-

from pyfakefs.fake_filesystem_unittest import Patcher as PyFakeFSPatcher


__all__ = ['FakeFS', 'PyFakeFSPatcher']

class FakeFS(object):
    def __init__(self, patcher):
        self._stubber = patcher

    def __getattr__(self, name):
        mapping = {
            'create_directory': self._stubber.fs.CreateDirectory,
        }
        if name in mapping:
            return mapping[name]
        klassname = self.__class__.__name__
        raise AttributeError("AttributeError: %s object has no attribute %r" % (klassname, name))
