from setuptools import setup, find_packages


classifiers = [

    'Development Status :: 1-Testing Stable',
    'Intended Audience :: Micropsi Team',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: MIT License',
    'Programming Language :: Python :: 3'
]

test_deps = [
    'unittest'
]

setup(
name='findmin',
version='0.0.1',
description='a basic implementation for findmin function',
long_description='Find the minimum using as few comparisons as possible. The array shall be given such that the first few elements are strictly monotonically decreasing, the remaining elements are strictly monotonically increasing. The less than operator be defined as the operator that works on such vectors where a < b if min(a,b) == a.',
url='',
author='Meriem Said',
author_email='saidmeriem96@gmail.com',
license='MIT',
classifiers=classifiers,
keywords='findmin',
packages=find_packages(exclude="tests"),
tests_require=test_deps,
install_requires=['']
)