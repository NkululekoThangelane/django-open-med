import os
from setuptools import setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-open-med',
    version='0.1',
    packages=[],
    license='GPL',
    description='A port of OpenEMR to django with a twist',
    author='Ben Waters',
    author_email='bsawyerwaters@gmail.com',
    classifiers=[
    ],
)
