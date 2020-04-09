import json
import os

default_cfg = {
    'root': os.path.join(os.path.expanduser('~'), "repositories"),
    'proj_schema': "{root}\\{tech}\\{proj_repo}\\{proj_root}",
    'repo_schema': "{root}\\{tech}\\{proj_repo}",
    'custom_schemas': {
        'default': [
            "+\\docs"
        ],
        'my_custom_schema': [
            "+\\custom_docs",
            "~\\common\\services"
        ],
    },
}


def load():
    cfg_path = os.path.join(os.path.expanduser('~'), os.path.join('.project_manager'))
    if not os.path.exists(cfg_path):
        os.makedirs(cfg_path)

        with open(os.path.join(cfg_path, 'config.json'), 'w') as config_file:
            config_file.write(json.dumps(default_cfg))

    with open(os.path.join(cfg_path, 'config.json'), 'r') as config_file:
        return json.load(config_file)

