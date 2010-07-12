from setuptools import setup, find_packages

setup(
    name = "whydjango",
    version = "0.1",
    url = 'http://github.com/pydanny/whydjango',
    license = 'BSD',
    description = "A site to promote django",
    author = 'Daniel Greenfeld',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)