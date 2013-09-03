#!/usr/bin/env python

from setuptools import setup, find_packages
 
setup (
    name='django-zipdistance',
    version='0.2.1',
    description='A zip code distance application for Django.',
    author='Elf M. Sternberg',
    author_email='elf.sternberg@gmail.com',
    url='http://github.com/elfsternberg/django-zipdistance/',
    license='MIT License',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Plugins',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires = ['django-classy-tags',],
    package_data = {
        '': ['*.json']
        },
    packages=find_packages(),
)
