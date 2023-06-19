"""Install script for setuptools."""

from setuptools import find_packages
from setuptools import setup
long_description = open("README.md").read()
setup(
    name='pyProject',
    version='0.0.1',
    description='',
    long_description =long_description,
    long_description_content_type='text/markdown',
    author='author',
    author_email='',
    license='MIT License',
    url='',
    packages=find_packages("src"),
    package_dir={"": "src"},
    python_requires = '3',
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        "Operating System :: Microsoft :: Windows",
        "Operating System :: MacOS",
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
