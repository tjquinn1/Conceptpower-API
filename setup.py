from distutils.core import setup

DISTNAME = 'conceptpower-python3-api'
AUTHOR = 'E. Peirson, Digital Innovation Group @ ASU'
MAINTAINER = 'T. Quinn Digital Innovation Group @ ASU'
MAINTAINER_EMAIL = "T. Quinn" <tjquinn1@asu.edu>
DESCRIPTION = ('A very simple library for querying a Conceptpower REST API.')
LICENSE = 'GNU GPL 3'
URL = 'https://github.com/erickpeirson/Conceptpower-API'
VERSION = '1.10'

PACKAGES = [ 'conceptpower',]

setup(
    name=DISTNAME,
    author=AUTHOR,
    author_email=MAINTAINER_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    description=DESCRIPTION,
    license=LICENSE,
    url=URL,
    version=VERSION,
    packages = PACKAGES,
    install_requires=[
        "requests",
    ],
)
