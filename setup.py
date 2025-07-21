from setuptools import setup
import setuptools

setup(
    name="PyBass",
    version="0.1",
    author="CheeZeDark",
    packages=setuptools.find_packages(),
    package_data={
        '': ['x64_bass\\*.dll'],
    }
)