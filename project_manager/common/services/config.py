import json
import os

def load():
    cfg_path = os.path.join(os.path.expand_user('~'), '.project_manager/config.json')
    if not os.path.exists(cfg_path):
        os.makedirs(cfg_path)
        default_cfg = {
            'root': os.path.join(os.path.expanduser('~'), "repositories"),
            'proj_schema': "{root}\\{tech}\\{proj_repo}\\{proj_root}",
            'repo_schema': "{root}\\{tech}\\{proj_repo}",
            'custom_schemas': [
                'default': [],
                'my_custom_schema': [],
            ]
        }

    with open(cfg_path) as config_file:
        return json.load(config_file)

