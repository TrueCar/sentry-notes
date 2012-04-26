#!/usr/bin/env python
"""
Setup for Sentry Notes Plugin
==============================

Adds the option to record simple plain-text notes to
message groups in sentry's GUI
"""

# See http://packages.python.org/distribute/setuptools.html
# for insight on how this works

from setuptools import setup, find_packages

setup(
    name="sentry-notes",
    version="0.1",
    license="3-clause BSD",
    description="Notation Tool for Sentry",
    long_description=__doc__,
    url="https://github.com/TrueCar/sentry-notes",
    author="Truecar.com Development Team",
    author_email="dev@truecar.com",
    maintainer="Ted Schundler",
    maintainer_email="tschundler@truecar.com",

    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    #package_data={'': ['*.txt', '*.html']},

    install_requires=[
        "sentry>=3.5.8",
    ],

)
