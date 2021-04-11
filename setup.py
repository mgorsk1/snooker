import os

from setuptools import find_packages, setup

__version__ = '0.0.0'

requirements_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'requirements.txt')

with open(requirements_path) as requirements_file:
    requirements = requirements_file.readlines()

setup(
    name='snooker',
    version=__version__,
    description='Snooker Data API',
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
