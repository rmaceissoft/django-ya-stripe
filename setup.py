import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-ya-stripe",
    version = "0.1",
    description = "Sync django models charged with stripe's charges",
    long_description = read('README.rst'),
    url = 'https://github.com/rmaceissoft/django-ya-stripe',
    author = 'Reiner Marquez',
    author_email = 'rmaceissoft@gmail.com',
    packages = find_packages(exclude=['tests', 'example', 'docs']),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires = ['stripe'],
)
  