from os import path
from setuptools import setup, find_packages


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


setup(
    name='aiospotipy',
    version='0.0.2',
    description='an API wrapper for Spotify',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author='sizumita',
    install_requires=['aiohttp'],
    url='https://github.com/sizumita/aiospotipy',
    license="MIT",
    packages=find_packages(),
    python_requires='>=3.5.3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: Japanese',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)