# setup.py

from setuptools import setup, find_packages

setup(
    name='math_util',                     # Name of your library
    version='0.1.0',                        # Version of your library
    packages=find_packages(),               # Automatically find packages
    install_requires=[],                    # List your library's dependencies
    author='Devasish Ghosh',
    author_email='dev.achieve@gmail.com',
    description='A simple example library', # Short description
    long_description=open('README.md').read(),  # Long description from README
    long_description_content_type='text/markdown', # Format of README
    url='https://github.com/devasish/studian',  # URL of the project
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',                # Python version compatibility
)
