from setuptools import setup

setup (
    name = 'jfrog-pypi-example',
    version = '1.0.0',
    description = 'Example PyPI package',
    py_modules = ["main"],
    package_dir = {'': 'src'},
    author = 'JFrog',
    author_email = 'jfrog@jfrog.com',
    url='https://github.com/jfrog/project-examples',
    install_requires=[
        'Django>=3.0',
        'Flask>=1.0',
        'MarkupSafe>=2.0',
    ],
)
