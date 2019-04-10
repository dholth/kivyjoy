#!/usr/bin/env python

from setuptools import setup

from distutils.command import build_ext

import codecs
README = codecs.open('README.rst', encoding='utf-8').read()
CHANGES = codecs.open('CHANGES.rst', encoding='utf-8').read()

setup(name="kivyjoy",
    version="0.10.0",
    packages=['kivyjoy', '_kivyjoy'],
    package_data={'_kivyjoy' : ['sdl.h', 'defines.h', 'sdlint.h']},
    setup_requires=["cffi>=1.10.0"],
    install_requires=['cffi>=1.10.0'],
    extras_require={
        'build':['pycparser', 'astor', 'cffi>=1.6.0'],
        'doc':['sphinx']
        },
    cffi_modules=[
        "_kivyjoy/cdefs.py:ffi",
        ],
    description="Limited SDL2 wrapper with cffi, to add improved gamepad support to Kivy",
    long_description=README + CHANGES,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)"
	],
    keywords=['sdl', 'cffi', 'kivy'],
    author="Daniel Holth",
    author_email="dholth@fastmail.fm",
    url="https://bitbucket.org/dholth/kivyjoy")
