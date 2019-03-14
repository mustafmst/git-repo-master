from git_repo_master.azure_devops.branch_locker import lock_branch, unlock_branch

ACTIONS = {
    'lock-branch': lock_branch,
    'unlock-branch': unlock_branch
}
