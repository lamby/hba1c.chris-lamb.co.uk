#!/usr/bin/env python

import os
import sys
import setuptest

from setuptools import setup, find_packages

NAME = 'hba1c'

def find_data_files(dirs):
    result = []
    for x in dirs:
        for dirpath, _, filenames in os.walk(x, followlinks=True):
            result.append((
                dirpath,
                [os.path.join(dirpath, y) for y in filenames],
            ))
    return result

setup(
    name=NAME,
    scripts=('%s/manage.py' % NAME,),
    cmdclass={'test': setuptest.test},
    packages=find_packages(),
    zip_safe=False,
    data_files=find_data_files(('media', 'templates')),
)
