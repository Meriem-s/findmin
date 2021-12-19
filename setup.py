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
long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
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