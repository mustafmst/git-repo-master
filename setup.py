from setuptools import setup, find_packages
import sys
import argparse

with open('README.md', 'r') as readme:
    long_desc = readme.read()

version = '0.1.3'

parser = argparse.ArgumentParser()
parser.add_argument('--build-no', help='build number for versioning')
args, unknown = parser.parse_known_args()

if args.build_no is not None:
    version = '{}.{}'.format(version, args.build_no)
    sys.argv.remove(args.build_no)
    sys.argv.remove('--build-no')

setup(
    name="git-repo-master",
    version=version,
    packages=find_packages(),
    author='Paweł Mstowski',
    entry_points={
        'console_scripts':['grm=git_repo_master.app:run']
    },
    author_email="pawel.mstowski@gmail.com",
    description='Small package to automate actions with git repo on Azure DevOps',
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url='https://github.com/mustafmst/git-repo-master',
    classifiers=[
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ],
)
