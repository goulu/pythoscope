import sys

try:
    from setuptools import setup
    install_requires = ['six','dill']
    args = dict(
        entry_points = {'console_scripts': ['pythoscope = pythoscope:main']},
        install_requires = install_requires,
        test_suite = 'nose.collector',
        tests_require = ['nose', 'mock', 'docutils'])
except ImportError:
    from distutils.core import setup
    args = dict(scripts = ['scripts/pythoscope'])


from pythoscope import __version__ as VERSION

setup(
    name='pythoscope',
    version=VERSION,

    author = 'Michal Kwiatkowski',
    author_email = 'constant.beta@gmail.com',
    description = 'unit test generator for Python',
    long_description = open("README.md").read() + "\n" + open("Changelog").read(),
    license = 'MIT',
    url = 'http://pythoscope.org',

    packages = ['pythoscope', 'pythoscope.inspector', 'pythoscope.generator',
                'bytecode_tracer'],
    package_data = {'pythoscope': [],
                    'bytecode_tracer': []},

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Testing',
    ],

    **args
)
