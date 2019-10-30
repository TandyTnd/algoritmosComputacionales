#!/usr/bin/env python
# -*- coding: utf-8 -*-

long_description = """\
randomdotorg.py is a python module to implement python's random number interface
by fetching data from random.org, which is is a true random number service
that generates randomness via atmospheric noise.

Example of use:

>>> r = randomdotorg.RandomDotOrg()
>>> r.get_quota() # method to get allowed bit quota for this ip
999171
>>> print r.randrange(2, 33, 3)
14

Methods supported by the standard library random module are supported, except
for save/load state and seeding which won't make sense for a true random number
generator.
"""

from randomdotorg import __version__

from distutils.core import setup
setup(name='randomdotorg', version=__version__, author='Clovis Fabricio',
      author_email='nosklo at gmail dot com', url='http://code.google.com/p/randomdotorg/',
      maintainer='Clovis Fabricio', maintainer_email='nosklo at gmail dot com',
      description='random.org number generator interface module',
      long_description=long_description,
      download_url='http://code.google.com/p/randomdotorg/downloads/list',
      py_modules=['randomdotorg'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Plugins',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU General Public License (GPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: Scientific/Engineering :: Mathematics',
          'Topic :: Utilities',
          ]
    )

