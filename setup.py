from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='solids',
    version='1.0.0',
    description='Generate solid backgrounds instantly',
    author='Danish Prakash',
    author_email='danishprakash@outlook.com',
    url='https://github.com/prakashdanish/solids',
    py_modules=['solids'],
    install_requires=[
        'requests',
        'pyperclip',
        'Pillow',
        'imgurpython'
    ],
    entry_points={
        'console_scripts': [
            'solids = solids:main'
        ],
    },
)
