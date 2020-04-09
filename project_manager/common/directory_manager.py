import os

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

def create_custom_schemas(cfg, args, repo_path, proj_path):
    schemas = cfg['custom_schemas']['default']
    if args.schema is not None:
        try:
            schemas = cfg['custom_schemas'][args.schema]
        except:
            print('{schema} does not exist in your config'.format(schema=args.schema))
            return

    for scheme in schemas:
        try:
            append_dir = repo_path if scheme[0] is '+' else proj_path if scheme[0] is '~' else None
            if append_dir is None:
                print('Invalid schema format')
                return

            os.makedirs(append_dir + scheme[1:])
        except FileExistsError:
            print("Failed to create {scheme}".format(scheme=scheme))