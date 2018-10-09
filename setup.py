from setuptools import setup
import os
import sys

_here = os.path.abspath(os.path.dirname(__file__))

if sys.version_info[0] < 3:
    with open(os.path.join(_here, 'README.rst')) as f:
        long_description = f.read()
else:
    with open(os.path.join(_here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()

version = {}
with open(os.path.join(_here, 'plainview_cli', 'version.py')) as f:
    exec(f.read(), version)

setup(
    name='plainview_cli',
    version=version['__version__'],
    description=('Command Line Interface for Plainview.'),
    long_description=long_description,
    author='Daniel Balagula',
    author_email='db2791@nyu.edu',
    url='https://github.com/bast/plainview_cli',
    license='MPL-2.0',
    packages=['plainview_cli'],
#   no dependencies in this example
    install_requires=[
        'requests==2.19.1',
        'appdirs==1.4.3',
        'jsonschema==2.6.0'
    ],
#   no scripts in this example
#   scripts=['bin/a-script'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'],
    entry_points={
        'console_scripts': [
            'plainview = plainview_cli.CommandLine:ExecuteCommand'
        ]
    }
) 
