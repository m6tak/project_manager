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
    else:
        print("New {tech} project created: {path}".format(tech=args.tech, path=paths['proj']))
        init_repo(paths['repo'], args.project_name)
        print("Git repository initialized with readme.md")
        
    additional_actions(args, paths['repo'])
        


def create_dirs(cfg, args):
    root  = cfg['root']
    proj_schema = cfg['proj_schema']
    repo_schema = cfg['repo_schema']
    repo_name = args.project_name if args.repo_name is None else args.repo_name
    proj_path = proj_schema.format(root=root, tech=args.tech, proj_repo=repo_name, proj_root=args.project_name)
    repo_path = repo_schema.format(root=root, tech=args.tech, proj_repo=repo_name)
    try:
        os.makedirs(proj_path)
        return {'proj': proj_path, 'repo': repo_path}
    except FileExistsError:
        return None

            

def init_repo(repo_path, project_name):
    with open(repo_path + '\\readme.md', 'w') as readme:
        readme.write('# {project_name}\n'.format(project_name=project_name))
    os.system('cd {path} && git init && git add . && git commit -m \"initial commit\"'.format(path=repo_path))

def additional_actions(args, repo_path):
    if args.open_vsc:
        os.system('cd {path} && code .'.format(path=repo_path))
    
    if args.open_dir:
        os.system('start {path}'.format(path=repo_path))

if __name__ == '__main__':
    run()

    

            
    
    
