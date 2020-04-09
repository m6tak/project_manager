import argparse

parser = argparse.ArgumentParser()
parser.add_argument('project_name', help='name of your project')
parser.add_argument('tech', help='main project technology')
parser.add_argument('--no_repo', action='store_true', help='switch for git repo initialization')
parser.add_argument('--repo_name', action='store', help='repository name')
parser.add_argument('--open_vsc', action='store_true', help='open repository with vs code')
parser.add_argument('--open_dir', action='store_true', help='open repository in file explorer (windows only)')
parser.add_argument('--schema', action='store', help='name of custom schema to use')

def parse():
    return parser.parse_args()

