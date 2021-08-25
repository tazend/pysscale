#!/usr/bin/env python

from setuptools import setup, find_packages
import pathlib

cwd = pathlib.Path(__file__).parent.resolve()

long_desc = (cwd / 'README.md').read_text(encoding='utf-8')

setup(
    name='pysscale',
    version='0.1',
    description='Python Wrapper for Spectrum Scale',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/tazend/pysscale',
    author='Toni Harzendorf',

    classifiers=[
        'License :: Apache License 2.0'

        'Programming Language :: Python :: 3',
    ],

    keywords='gpfs, spectrumscale, filesystem, hpc',

    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=[],

    project_urls={
        'Bug Reports': 'https://github.com/tazend/pysscale/issues',
        'Source': 'https://github.com/tazend/pysscale',
    },
)
