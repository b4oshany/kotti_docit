import os

from setuptools import setup
from setuptools import find_packages

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''
try:
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except IOError:
    CHANGES = ''

version = '0.0.1'

install_requires = [
    'Kotti>=1.0.0',
    'kotti_tinymce',
    'progress',
    'markdown',
    'funcsigs',
    'transaction',
    'pyramid_tm',
    'pyramid_celery',
    'unicodecsv==0.14.1',
    'kotti_pdf>=0.3.5',
    'kotti_survey>=0.2.8',
    'kotti_google_analytics==1.1.20',
    'kotti_alert>=0.2.5',
    'click>=6.6',
]


setup(
    name='kotti_docit',
    version=version,
    description="Documentation site for your Kotti site",
    long_description='\n\n'.join([README, CHANGES]),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Framework :: Pylons",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        "License :: Repoze Public License",
    ],
    author='Oshane Bailey',
    author_email='b4.oshany@gmail.com',
    url='https://github.com/b4oshany/kotti_docit',
    keywords='kotti web cms wcms pylons pyramid sqlalchemy bootstrap',
    license="BSD-derived (http://www.repoze.org/LICENSE.txt)",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=[],
    dependency_links=[],
    entry_points={
        'fanstatic.libraries': [
            'kotti_docit = kotti_docit.fanstatic:library',
        ],
    },
    extras_require={},
)
