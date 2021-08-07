# project-automation

## Getting Started
To setup up this automation:

```
Generate a github token, if you plan to setup this project in remote
```


### Pre-setup
```
create env variables
> set project directory as 'ProjectPath'
> set github token as 'GitToken'
```

### Project Setup

```
git clone "https://github.com/sachinpjose/projectInitializerAutomation.git"
cd project-automation
pip install -r requirements.txt

path:
Add "project-automation" folder directory to path in environment variable.
```

### Usage

```
Command to run the program type

To run the automation.
'create <project_name>' - By default a repo will be created in github in private mode.
'create <project_name> -m/--mode local'   - To setup a git project structure in local.

Additional commands
'create <project_name> -p/--private n' - for creating repo in public mode, if not mentioned will create as private.
'create <project_name> -e/--editor y' - To open the code in editor after the project is created.
```

