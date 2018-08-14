from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='chromatic',
    version='1.0.3',
    description='Generate monochromatic backgrounds instantly',
    long_description=long_description,
    author='Danish Prakash',
    author_email='danishprakash@outlook.com',
    url='https://github.com/prakashdanish/chromatic',
    packages=['chromatic'],
    install_requires=[
        'requests',
        'pyperclip',
        'Pillow',
        'imgurpython'
    ],
    entry_points={
        'console_scripts': [
            'chromatic = chromatic.chromatic:main'
        ],
    },
)
