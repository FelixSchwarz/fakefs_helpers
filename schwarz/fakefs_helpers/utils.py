# -*- coding: utf-8 -*-
# SPDX-License-Identifier: MIT or CC0-1.0

import os


__all__= ['is_pathlike']

def is_pathlike(path):
    if hasattr(os, 'PathLike') and isinstance(path, os.PathLike):
        return True
    return not hasattr(path, 'startswith')

