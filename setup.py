from setuptools import setup, find_packages

setup(
    name="git-repo-master",
    version="0.1.3",
    packages=find_packages(),
    entry_points={
        'console_scripts':['grm=git_repo_master.app:run']
    }
)
