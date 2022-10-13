# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT or CC0-1.0

import os


__all__= ['is_pathlike', 'make_string_path']

def is_pathlike(path):
    if hasattr(os, 'PathLike') and isinstance(path, os.PathLike):
        return True
    return not hasattr(path, 'startswith')

def make_string_path(path):
    if not is_pathlike(path):
        return path
    return str(path)
