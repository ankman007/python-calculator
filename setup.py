from setuptools import setup, find_packages

setup(
    name="simple-calculator",
    version="0.1",
    packages=find_packages(),
    entry_point={
        'console-scripts': [
            'simple_calculator=calculator:calculator',
        ]
    },
    author="ankman",
    author_email="",
    install_requires=[],
)