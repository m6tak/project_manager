import argparse

parser = argparse.ArgumentParser()
parser.add_argument('project_name', help='name of your project')
parser.add_argument('tech', help='main project technology')
parser.add_argument('--no_repo', action='store_true', help='switch for git repo initialization')
parser.add_argument('--repo_name', action='store', help='repository name')


def parse():
    return parser.parse_args()

