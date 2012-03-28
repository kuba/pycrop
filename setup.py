import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(
    name='pycrop',

    description="Generate square thumbnails using improved reddit's smart-cropping.",
    long_description=README,
    keywords='thumbnail smart cropping entropy reddit',
    classifiers=(
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Utilities',
    ),

    author='christopherhan',
    url='https://github.com/kuba/pycrop',

    py_modules=['pycrop'],
    include_package_data=True,

    setup_requires=[
        'setuptools_git', # Instead of MANIFEST.in
    ],
    install_requires=[
        'PIL',
    ],
)
