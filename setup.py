#!/usr/bin/env python
import re

from setuptools import setup


def requires_from_file(filename):
    requirements = []
    with open(filename, 'r') as requirements_fp:
        for line in requirements_fp.readlines():
            match = re.search('^\s*([a-zA-Z][^#]+?)(\s*#.+)?\n$', line)
            if match:
                requirements.append(match.group(1))
    return requirements


setup(
    tests_require = requires_from_file('dev_requirements.txt'),
    install_requires=requires_from_file('requirements.txt'),
)

