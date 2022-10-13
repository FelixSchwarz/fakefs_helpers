# -*- coding: utf-8 -*-
# The source code contained in this file is licensed under the MIT license or
# (at your option) the CC0 v1.0.
# SPDX-License-Identifier: MIT or CC0-1.0

try:
    from pathlib import Path
except ImportError:
    from pathlib2 import Path
from unittest import TestCase

from schwarz.fakefs_helpers import TempFS


class TempFSTest(TestCase):
    def setUp(self):
        self.fs = TempFS.set_up(test=self)

    def test_create_directory_with_path_instance(self):
        path = Path('/foo')
        result = self.fs.create_directory(path)
        assert Path(result).is_dir()
