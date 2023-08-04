from github import Github
import json

from flask import Flask
from flask import request

app = Flask(__name__)
@app.route('/gitgpt', methods=['GET']) # http://localhost:5000/gitgpt?repo_name=huyangliu/snake
def get_gitgpt():
    repo_name = request.args.get('repo_name')
    # print(repo_name)
    # Use parameters from json file  {"access_token": "xxxxxxxxxxxx"}
    with open('parameters.json', 'r') as f:
        config = json.load(f)
    # Authenticate with personal access token
    access_token = config["access_token"]
    g = Github(access_token)

    # Get the repository
    # repo_name = config["repo_name"]
    repo = g.get_repo(repo_name)

    # Browse the files
    contents = repo.get_contents("")
    # filter the files
    filtered_files = filter_files(contents)

    data = []
    for file in filtered_files:
        # print(file.path)
        if file.type == "dir":
            filtered_files.extend(repo.get_contents(file.path))
        else:
            print(file)
            file_data = {"filename": file.name,
                    "contents": str(file.decoded_content)}
            # print(file.path)
            # print(file.decoded_content)
            data.append(file_data)
        # Code to handle the GET request goes here
    return data


def filter_files(files):
    
    # Define a list of unnecessary file extensions
    ignore_extensions = ['.dll', '.exe', '.jpg', '.jpeg', '.png', '.gif', '.csv', '.gitignore', '.md', 'LICENSE']

    # Define a list of unnecessary file paths
    ignore_paths = ['libs', 'lib', 'data', 'docs', 'images', 'img']

    # Filter the files
    filtered_files = [file for file in files if
                      not any(file.path.endswith(ext) for ext in ignore_extensions)
                      and not any(path in file.path for path in ignore_paths)]

    return filtered_files




# with open('data.json', 'w') as f:
#     json.dump(data, f)

if __name__ == '__main__':
    app.run()