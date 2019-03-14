import argparse

from git_repo_master.azure_actions import ACTIONS


def startup_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group('All arguments')
    group.add_argument('-organization', help='Azure DevOps organization')
    group.add_argument('-project', help='Azure DevOps project in given organization')
    group.add_argument('-repository', help='Repo for action', nargs='+')
    group.add_argument('-token', help='Personal access token for Azure DevOps')
    group.add_argument('-branch', help='Branch to perform action on')
    group.add_argument('-from', help='Branch name from which action has to be done')
    group.add_argument('-to', help='Branch name to which action has to be done')
    group.add_argument('-title', help='Pull request title')
    group.add_argument('-description', help='Pull request description')
    group.add_argument('-action', help='Action to perform', choices=ACTIONS.keys())

    args = parser.parse_args()
    return args


def main():
    args = startup_parser()
    if args.action in ACTIONS:
        ACTIONS[args.action](args)
    else:
        print('Nothing to do.')


if __name__ == '__main__':
    main()
