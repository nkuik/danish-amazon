from setuptools import setup

dependencies = []

setup(
    name="danish-",
    version="0.1",
    author="Nathan Kuik",
    author_email="nathan@nathankuik.com",
    description="Order things from nemlig",
    install_requires=dependencies,
    packages=[],
    entry_points={
        'console_scripts': [
            'danish-amazon = danish-amazon.main:run',
       ]
    },
    url="https://bitbucket.org/twyla/xpi",
)
