from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name='bidoptimizer',
    version='0.1',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=required,
    entry_points={
        'console_scripts': [
            'bidoptimizer = src.main:main',
        ],
    },
)
