from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='circuitroomba',

    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    description='CircuitPython helper library for interfacing with Roomba Open Interface devices.',
    long_description=long_description,
    long_description_content_type='text/x-rst',

    url='https://gitlab.com/AlexanderHagerman/circuitroomba',

    author='Alexander Hagerman',
    author_email='alex@unexpectedeof.net',

    install_requires=[
        'Adafruit-Blinka'
    ],

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='adafruit blinka circuitpython micropython circuitroomba roomba robot automation',

    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
