import sys
import os
import common.services.config as config
import common.services.arg_processor as arg_processor

def run():
    cfg = config.load()
    args = arg_processor.parse()
    paths = create_dirs(cfg, args)
    if paths is None:
        print("Project with that name already exists")
        exit(0)

    if args.no_repo:
        print("New {tech} project created: {path}".format(tech=args.tech, path=paths['proj']))
        exit(0)
    else:
        print("New {tech} project created: {path}".format(tech=args.tech, path=paths['proj']))
        init_repo(paths['repo'], args.project_name)
        print("Git repository initialized with readme.md")
        


def create_dirs(cfg, args):
    root  = cfg['root']
    proj_schema = cfg['proj_schema']
    repo_schema = cfg['repo_schema']
    proj_path = proj_schema.format(root=root, tech=args.tech, proj_repo=args.project_name, proj_root=args.project_name)
    repo_path = repo_schema.format(root=root, tech=args.tech, proj_repo=args.project_name)
    print(proj_path)
    print(repo_path)
    try:
        os.makedirs(proj_path)
        return {'proj': proj_path, 'repo': repo_path}
    except FileExistsError:
        return None

            

def init_repo(repo_path, project_name):
    with open(repo_path + '\\readme.md', 'w') as readme:
        readme.write('# {project_name}\n'.format(project_name=project_name))
    os.system('cd {path} && git init && git add . && git commit -m \"initial commit\"'.format(path=repo_path))

if __name__ == '__main__':
    run()

    

            
    
    
