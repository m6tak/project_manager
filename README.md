# project_manager
project_manager is exactly what it says. Simple python tool that speeds up starting up your project by creating directory structure in organized way.
Just fire up your shell, run one command and get started :)

# How does it work?

### Command structure
**Legend**:
* {} required argument
* [] optional argument

```
pm {project_name} {project_technology_name} [--repo_name NAME] [--no_repo] [--open_vsc] [--open_dir]
```

This command generates following output:
```
root
    |
    |- {project_technology_name} (folder wher all related project are going to be stored)
        |
        | - {project_name} (repo folder)
            |
            | - .git (optional)
            | - readme.md (optional)
            | - {project_name} (project root)
```

### Optional parameters
* *--open_vsc*: runs shell `cd {path} && code .`
* *--open_dir*: **windows only** runs shell `start {path}` ie. opens repo path in file explorer

# Configuration

### This is your config.json
```
{
    "root": "C:\\Users\\48570\\Desktop\\projekty",
    "proj_schema": "{root}\\{tech}\\{proj_repo}\\{proj_root}",
    "repo_schema": "{root}\\{tech}\\{proj_repo}",
    "custom_schemas": []
}
```
* *root*: root directory for your projects
* *proj_schema*: where your project root should be located
* *repo_schema*: where git repository should be initialised

### Schema keywords
* *root*: cooresponds to root directory set in config
* *tech* cooresponds to {project_technology_name} argument
* *proj_repo* cooresponds to {project_name} argument unless specified with --repo_name argument
* *proj_name* cooresponds to {project_name} agument

### Custom schemas
Custom schema lets you create additional directory structure inside your repository.
Just add paths you want do create to the array in your config file.
Remember to add `\\` or `/` at the begining of your scheme as it gets appended to path exactly like you type it.
```
{
    ...
    "custom_schemas": [
        "\\docs\\api",
        "\\docs\\somefolder\\otherfolder",
        "\\somethingelse\\anything"
    ]
}
```
Will give following result:

```
root
    |
    |- {project_technology_name} (folder wher all related project are going to be stored)
        |
        | - {project_name} (repo folder)
            |
            | - .git (optional)
            | - readme.md (optional)
            | - {project_name} (project root)
            | - docs
            |   |-api
            |   |-somefolder
            |       |-otherfolder
            |
            | - somethingelse
                |-anything
```

# Requirements
* **Python version:** 3.7

### Optional
* git client
* vs code

**Enjoy :)**
