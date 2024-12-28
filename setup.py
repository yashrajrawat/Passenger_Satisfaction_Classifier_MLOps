from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = 'airline_passenger_satisfaction-mlops',
    version = '0.1',
    author = 'yashraj singh rawat',
    author_email = 'yashrajrawat733@gmail.com',
    description = 'MLOPS Project',
    packages = find_packages(),
    install_requires = requirements,
    python_requires = '>=3.7'
)