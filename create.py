import os
import argparse
from remote import remote_project
from local import local_project

parser = argparse.ArgumentParser()

parser.add_argument('project', type=str,
                    help='A required argument for project name')

parser.add_argument('-m', '--mode', choices=['remote', 'local'], default='remote',
                    help='An optional for creating project either local or remote.')

parser.add_argument('-p', '--private', choices=['y', 'n'], default="y",
                    help='A boolean to create repo in private mode or not.')

parser.add_argument('-e', '--editor', choices=['y', 'n'], default="n",
                    help='A boolean to create repo in private mode or not.')

parser.add_argument('-i', '--idle', choices=['vs', 'pycharm'], default="pycharm",
                    help='Supports VS code or Pycharm as IDLE. Default is set as pycharm')

args = parser.parse_args()

project = args.project
mode = args.mode
private = True if args.private == "y" else False
editor = True if args.editor == "y" else False
idle = args.idle

if mode == "remote":
    project_path = remote_project(project, private)
    print("Project Setup completed.")
else:
    project_path = local_project(project)
    print("Project Setup completed.")

if editor:
    if idle == "pycharm":
        os.system(f"pycharm64.exe {project_path}")
    else:
        os.system(f"code -n {project_path}")



