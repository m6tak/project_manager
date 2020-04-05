# project_manager
project_manager is exactly what it says. Simple python tool that speeds up starting up your project by creating directory structure in organized way.
Just fire up your shell, run one command and get started :)

# How does it work?

### Command structure
**Legend**:
* {} required argument
* [] optional argument

```
pm {project_name} {project_technology_name} [--repo_name NAME] [--no_repo] 
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

# Configuration

### This is your config.json
```
{
    "root": "C:\\Users\\48570\\Desktop\\projekty",
    "proj_schema": "{root}\\{tech}\\{proj_repo}\\{proj_root}",
    "repo_schema": "{root}\\{tech}\\{proj_repo}"
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

# Requirements
* **Python version:** 3.7

**Enjoy :)**
