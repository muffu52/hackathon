import json



def file_organization_sentence():
    """ 
    This function is used to generate the sentences that describe the file organization of a repository.
    It reads the file organization from a JSON file and generates a list of sentences to describe the repository architecture.
    """
    # Read the file organization from the JSON file
    with open('paths.json', 'r') as json_file:
        file_organization = json.load(json_file)

    # Create a dictionary to group files by folders
    folder_structure = {}

    # Group files by folders
    for file_path in file_organization:
        folders = file_path.split('/')
        if len(folders) > 1:
            folder = folders[0]
            if folder not in folder_structure:
                folder_structure[folder] = []
            folder_structure[folder].append(file_path)
        else:
            if 'files' not in folder_structure:
                folder_structure['files'] = []
            folder_structure['files'].append(file_path)

    # Generate the grouped sentences
    sentences = []
    for folder, files in folder_structure.items():
        sentence = ""
        if folder == 'files':
            file_list = ', '.join(files)
            sentence = f"In the repository there {'is' if len(files) == 1 else 'are'} {file_list} {'file' if len(files) == 1 else 'files'}."
        else:
            sentence = f"In the repository there is also the folder'{folder}', in {folder} there {'is' if len(files) == 1 else 'are'} "
            file_list = ', '.join(files)
            sentence += file_list + '.'
        sentences.append(sentence)

    # Print the grouped sentences
    for sentence in sentences:
        print(sentence)
    with open('sentences.json', 'w') as f:
        json.dump(sentences, f)
        
file_organization_sentence()