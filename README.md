# project_manager
project_manager is exactly what it says. Simple python tool that speeds up starting up your project by creating directory structure in organized way.  
Just fire up your shell, run one command and get started :)

# How does it work?

### Command structure
**Legend**:
* {} required argument
* [] optional argument

```
pm {project_name} {project_technology_name} [--repo_name NAME] [--no_repo] [--schema NAME] [--open_vsc] [--open_dir]
```

`pm my_project python` generates following output:
```
root
    |
    |- python (folder wher all related projects are going to be stored)
        |
        | - my_project (repo folder)
            |
            | - .git (optional)
            | - readme.md (optional)
            | - my_project (project root, here goes all the code stuff)
```

### Optional parameters
* *--open_vsc*: runs shell `cd {path} && code .`
* *--open_dir*: **windows only** runs shell `start {path}` ie. opens repo path in file explorer
* *--repo_name*: lets you specify repository name diffrent than project name. If repository with that name exists new project will be added there
* *--schema*: lets you specify schema of your initial directory structure stored in your config file by its name
* *--no_repo*: switch for git repository initialization

# Configuration

### This is your config.json

It's located in your home directory in .project_manager folder

```
{
    "root": *your home directory path*\\repositories,
    "proj_schema": "{root}\\{tech}\\{proj_repo}\\{proj_root}",
    "repo_schema": "{root}\\{tech}\\{proj_repo}",
    "custom_schemas": {
        "default": [
            "+\\docs"
        ],
        "my_custom_schema": [
            "+\\custom_docs",
            "~\\common\\services"
        ],
    },
}
```
* *root*: root directory for your projects
* *proj_schema*: where your project root should be located
* *repo_schema*: where git repository should be initialised
* *custom_schemas*: place when you can put your custom directory structure templates

### Schema keywords
* *root*: cooresponds to root directory set in config
* *tech* cooresponds to {project_technology_name} argument
* *proj_repo* cooresponds to {project_name} argument unless specified with --repo_name argument
* *proj_name* cooresponds to {project_name} agument

### Custom schemas
Custom schema lets you create additional directory structure inside your repository.
Remember to add `\\` or `/` at the begining of your scheme as it gets appended to path exactly like you type it.
* Add `+` to the beggining of the path if you want structure appended to repository folder
* Add `~` to the beggining of the path if you want structure appended to project root folder
* **NOTE**: `+` or `~` **MUST** be specified  
You can store any number of custom schemas you like and than just choose any with `--schema {NAME}` parameter
```
{
    ...
    "custom_schemas": {
        "default": [
            "+\\docs"
        ],
        "my_custom_schema": [
            "+\\custom_docs",
            "~\\common\\services"
        ],
    },
}
```


If you dont specify schema with parameter, default one is used so you might want to leave it empty  
Running `pm {project_name} {project_technology_name} --schema my_custom_schema` Will give following result:

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
            |   | - common
            |   |   | - services
            |
            | - custom_docs

```
# Planned features
* [ ] Add user defined commands to be run in the repository/project root

# Requirements
* **Python version:** 3.7

### Optional
* git client
* vs code

# Installation
You can find exe build [here](https://drive.google.com/open?id=13CdW9Mc5eTw8AvGQi_nhWaGs90GBXzbf)  
If you want you can add it to path and use it this way:  
`pm.exe ...`  
I also included setup.bat which installs project_manager as shell command so you can do just  
`pm ...`

**Disclaimer** This was tested on windows ONLY.

# Credits
Thanks to @koflus for help with shell scripts and overall setup:)

**Enjoy :)**
