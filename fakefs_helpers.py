# -*- coding: utf-8 -*-



__all__ = ['FakeFS']

class FakeFS(object):
    def __init__(self, patcher):
        self._stubber = patcher

    @classmethod
    def set_up(cls, test=None):
        # only require pyfakefs if it is actually used
        from pyfakefs.fake_filesystem_unittest import Patcher
        stubber = Patcher()
        stubber.setUp()
        if test:
            test.addCleanup(stubber.tearDown)
        return FakeFS(stubber)

    def tear_down(self):
        self._stubber.tearDown()

    def __getattr__(self, name):
        mapping = {
            'create_directory': self._stubber.fs.CreateDirectory,
            'create_file': self._stubber.fs.CreateFile,
        }
        if name in mapping:
            return mapping[name]
        klassname = self.__class__.__name__
        raise AttributeError("AttributeError: %s object has no attribute %r" % (klassname, name))
