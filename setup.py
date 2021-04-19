import os

from setuptools import find_packages, setup

__version__ = '0.5.0'

requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')
readme_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'README.md')

with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

with open(readme_path) as readme_file:
    long_description = readme_file.read()

setup(
    name='snooker',
    version=__version__,
    description='Snooker Data API',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.github.com/mgorsk1/snooker',
    maintainer='mgorsk1',
    maintainer_email='gorskimariusz13@gmail.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements,
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
