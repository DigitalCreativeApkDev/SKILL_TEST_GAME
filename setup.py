from setuptools import setup


def readme():
    with open("README.md", "r") as fh:
        long_description = fh.read()
        return long_description


setup(
    name='SKILL_TEST_GAME',
    version='1',
    packages=['SKILL_TEST_GAME'],
    url='https://github.com/DigitalCreativeApkDev/SKILL_TEST_GAME',
    license='MIT',
    author='DigitalCreativeApkDev',
    author_email='digitalcreativeapkdev2022@gmail.com',
    description='This package contains implementation of the game "Skill Test Game". This game '
                'is about taking skill tests and earning skill badges.',
    long_description=readme(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7"
    ],
    entry_points={
        "console_scripts": [
            "SKILL_TEST_GAME=SKILL_TEST_GAME.skill_test_game:main",
        ]
    }
)