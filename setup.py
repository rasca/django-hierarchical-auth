from distutils.core import setup

setup(
    name='django-hierarchical-auth',
    version='0.1.dev',
    author='Ivan Raskovsky (rasca)',
    author_email='raskovsky@gmail.com',
    packages=['hierarchical_auth',],
    # license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='Extends django auth allowing hierarchical permissions',
    long_description=open('README.txt').read(),
)
