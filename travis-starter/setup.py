# -*- coding: utf-8 -*-

from os import path

from setuptools import setup

# Long Description
with open(path.join(path.dirname(__file__), 'README.md')) as readme_file:
    LONG_DESCRIPTION = readme_file.read()

setup(
    name='sample_lib',
    version=1,
    description='A sample for pytest and travis',
    long_description=LONG_DESCRIPTION,
    author='Youssef Sherif',
    author_email='dday376@gmail.com',
    url='https://github.com/youssefsharief/py-test-starter',
    packages=[
        'sample_lib'
    ],
    package_dir={'sample_lib': 'sample_lib'},
    package_data={
        '': ['*.md'],
        'sample_lib': [
            '__init__.py',
        ]
    },
    include_package_data=True,
    zip_safe=False,
    license='GPL-3.0',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    )
)
