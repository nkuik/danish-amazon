from setuptools import setup

dependencies = []

setup(
    name="danish-amazon",
    version="0.1",
    author="Nathan Kuik",
    author_email="nathan@nathankuik.com",
    description="Order things from nemlig",
    install_requires=dependencies,
    packages=[],
    entry_points={
        'console_scripts': [
            'danish-amazon = main:run',
       ]
    },
    url="https://github.com/nkuik/danish-amazon",
)
