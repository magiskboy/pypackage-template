from setuptools import setup


with open('./README.md', 'r') as fi:
    readme = fi.read()

setup(
    name='{{cookiecutter.name}}',
    version='{{cookiecutter.version}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    packages=['{{cookiecutter.name}}'],
    description='{{cookiecutter.description}}',
    long_description=readme,
    long_description_content_type='text/markdown',
)
