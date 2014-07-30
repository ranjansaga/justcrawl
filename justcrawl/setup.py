from setuptools import setup, find_packages

setup(
    name='justcrawl',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = justcrawl.settings']},
)
