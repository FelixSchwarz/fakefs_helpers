#!/usr/bin/env python
import re

from setuptools import setup, find_packages


def requires_from_file(filename):
    requirements = []
    with open(filename, 'r') as requirements_fp:
        for line in requirements_fp.readlines():
            match = re.search('^\s*([a-zA-Z][^#]+?)(\s*#.+)?\n$', line)
            if match:
                requirements.append(match.group(1))
    return requirements


setup(
    name='FakeFSHelpers',
    version='1.1',

    author='Felix Schwarz',
    author_email='info@schwarz.eu',
    license='MIT',

    zip_safe=False,
    packages=find_packages(),
    namespace_packages = ['schwarz'],
    include_package_data=True,

    tests_require = requires_from_file('dev_requirements.txt'),
    install_requires=requires_from_file('requirements.txt'),
)

