
from setuptools import setup, find_packages


entrypoints = {}
entrypoints['console_scripts'] = [
    'digoie = digoie.__main__:main',
]

setup(
    name = 'digoie',
    version = '0.0.3',
    packages = find_packages(),
    entry_points = entrypoints
    )