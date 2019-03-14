import argparse

from git_repo_master.azure_actions import ACTIONS


def startup_parser():
    parser = argparse.ArgumentParser()
    group = parser.add_argument_group('Required Arguments')
    group.add_argument('-organization', help='Azure DevOps organization', required=True)
    group.add_argument('-project', help='Azure DevOps project in given organization', required=True)
    group.add_argument('-repository', help='Repo for action', required=True, nargs='+')
    group.add_argument('-token', help='Personal access token for Azure DevOps', required=True)
    group.add_argument('-branch', help='Branch to perform action on', required=True)
    group.add_argument('-action', help='Action to perform', required=True, choices=ACTIONS.keys())

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
