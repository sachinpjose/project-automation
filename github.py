import requests
import json
import sys


class Github:

    def __init__(self, token):
        self.token = token

    def create_repo(self, project_name, private=True):
        url = "https://api.github.com/user/repos"

        payload = json.dumps({
            "name": project_name,
            "description": project_name,
            "homepage": "https://github.com",
            "private": private,
            "has_issues": True,
            "has_projects": True,
            "has_wiki": True
        })
        headers = {
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        if response.status_code != 201:
            response_msg = json.loads(response.text)["errors"][0]["message"]
            if response_msg == "name already exists on this account":
                print(f"Repo with the name {project_name} already exists on this account.\n"
                      f"Please a create project with different name.")
                return False

            print("Please check your github token.")
            sys.exit()

        self.clone = json.loads(response.text)['clone_url']
        return True
