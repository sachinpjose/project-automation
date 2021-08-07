import sys
import os
from github import Github


def remote_project(project, private):

    try:
        folder = os.environ['ProjectPath']
        token = os.environ['GitToken']
    except:
        print("Create project folder and Github token in environment variables.")
        sys.exit()

    if os.path.isdir(folder):

        project_path = os.path.join(folder, project)

        if os.path.exists(project_path):
            while os.path.exists(project_path):
                project = input("Project name already exists. Please enter a different project name:")
                project_path = os.path.join(folder, project)

        os.mkdir(project_path)

        github = Github(token)
        if not github.create_repo(project, private=private):
            os.rmdir(project_path)
            sys.exit()

        commands = [f'echo "# {project}" >> README.md',
                    'git init',
                    f'git remote add origin {github.clone}',
                    'git add *',
                    'git commit -m "committing readme file"',
                    'git push -u origin master']

        os.chdir(project_path)
        for c in commands:
            os.system(c)
        return project_path

    else:
        print("Please set a valid project folder name in environment variables.")
