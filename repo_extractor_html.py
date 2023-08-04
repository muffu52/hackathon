from github import Github
import json


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


def generate_list_items(repo,items):
    html = '<ul>'
    for item in items:
        if item.type == "file":
            html += "<li>" + item.name + "</li>"
        elif item.type == "dir":
            html += '<li class="directory">' + item.name
            subitems = repo.get_contents(item.path)
            html += generate_list_items(repo,subitems)
            html += "</li>"
    html += "</ul>"
    return html
def extractor_html():
    # Use parameters from json file  {"access_token": "xxxxxxxxxxxx","repo_name":"xxxxx/xxxx"}
    with open('parameters.json', 'r') as f:
        config = json.load(f)

    # Authenticate with personal access token
    access_token = config["access_token"]
    g = Github(access_token)

    # Get the repository
    repo_name = config["repo_name"]
    repo = g.get_repo(repo_name)

    # Browse the files
    contents = repo.get_contents("")
    # filter the files
    filtered_files = filter_files(contents)
    # print(filtered_files)
    # data = []
    # paths = []
    html = generate_list_items(repo,filtered_files)
    return html
    # for file in filtered_files:
    #     if file.type == "dir":
    #         filtered_files.extend(repo.get_contents(file.path))
    #     else:
    #         print(file)
    #         file_data = {"filename": file.name,
    #                 "contents": str(file.decoded_content)}
    #         # print(file.path)
    #         # print(file.decoded_content)
    #         data.append(file_data)
    #         paths.append(file.path)
        
# with open('data.json', 'w') as f:
#     json.dump(data, f)
# with open('paths.json', 'w') as f:
#     json.dump(paths, f)
