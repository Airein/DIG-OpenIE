# Setup Configuration Reference
# Need to removed after public
# http://peterdowns.com/posts/first-time-with-pypi.html
# http://www.360doc.com/content/14/0306/11/13084517_358166737.shtml
# http://python-packaging-user-guide.readthedocs.org/en/latest/distributing/
# https://docs.python.org/2/distutils/setupscript.html
# https://wiki.python.org/moin/TestPyPI


"""Setup

sudo python setup.py install --record files.txt
cat files.txt | sudo xargs rm -rf

pip install -i https://testpypi.python.org/pypi digoie

"""


from setuptools import setup, find_packages


entrypoints = {}
entrypoints['console_scripts'] = [
    'digoie = digoie.__main__:main',
]

setup(
    name = 'digoie',
    version = '0.1.0',
    description = 'A Open Information Extraction Library',
    author = 'Peter Downs',
    author_email = 'zwein27@gmail.com',
    url = 'https://github.com/Airein/DIG-OpenIE',
    packages = find_packages(),
    entry_points = entrypoints,
    package_data={'digoie': ['res/*']},
    install_requires=['scikit-learn']
    )