# -*- coding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

import os


def read(*pathnames):
    return open(os.path.join(os.path.dirname(__file__), *pathnames)).read()


setup(
    name='collective.superfish',
    version='1.1.1.dev0',
    description="A suckerfish/superfish integration into plone",
    long_description='\n'.join([
        read('README.rst'),
        read('docs', 'TODO.txt'),
        read('docs', 'HISTORY.txt'),
        read('docs', 'THANKS.txt'),
    ]),
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
    ],
    keywords='navigation suckerfish superfish jquery dropdown',
    author='Daniel Widerin',
    author_email='daniel.widerin@kombinat.at',
    url='http://svn.plone.org/svn/collective/collective.superfish',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['collective'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        # -*- Extra requirements: -*-
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
