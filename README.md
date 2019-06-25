# git-repo-master

Simple application to manage your Azure DevOps git repository

## Installation

``` bash
git clone https://github.com/mustafmst/git-repo-master.git
python git-repo-master/setup.py install
```

## Usage

```bash
$ grm -h

usage: grm.py [-h] -organization ORGANIZATION -project PROJECT -repository
              REPOSITORY [REPOSITORY ...] -token TOKEN -branch BRANCH -action
              {lock-branch,unlock-branch}

optional arguments:
  -h, --help            show this help message and exit

Required Arguments:
  -organization ORGANIZATION
                        Azure DevOps organization
  -project PROJECT      Azure DevOps project in given organization
  -repository REPOSITORY [REPOSITORY ...]
                        Repo for action
  -token TOKEN          Personal access token for Azure DevOps
  -branch BRANCH        Branch to perform action on
  -action {lock-branch,unlock-branch}
                        Action to perform

```
