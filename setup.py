from setuptools import setup

dependencies = ['sanic', 'pyyaml', 'aiohttp']
test_dependencies = ['pytest', 'mock']

setup(
    name="slack-client",
    version="0.1",
    author="Nathan Kuik",
    author_email="nathan@nathankuik.com",
    description="Do things with Slack",
    install_requires=dependencies,
    tests_require=test_dependencies,
    test_suite='pytest',
    entry_points={
        'console_scripts': [
            'slack-client = main:run',
       ]
    },
    url="https://github.com/nkuik/slack-client",
)
