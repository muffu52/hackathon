from codes.repo_extractor import extractor
from codes.prompt_engineering import prompt_engine
from codes.repo_extractor_html import extractor_html
from codes.readme_generator_func import *
from flask import Flask, render_template, url_for, request, jsonify
import markdown

parser = argparse.ArgumentParser()
parser.add_argument('--openai_key' , help='OpenAI API key')
args = parser.parse_args()
openai_key  = args.openai_key

app = Flask(__name__, template_folder='../templates',static_folder='../static')

data = []
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/handle_form', methods=['POST'])
def handle_form():
    repo_name = request.form['name']
    global data
    data = []
    html, data = extractor_html(repo_name, 'data/parameters.json')
    print(repo_name)
    return jsonify({'list':html})

@app.route('/generateReadme', methods=['POST'])
def generateReadme():
    # print("generateReadme clicked", data)
    markdown = generate_readme(data,openai_key)
    # markdown = "# Hello I'm a mark down" #function()
    return jsonify({'md': markdown})
    # return jsonify({'name': name, 'list':html})

@app.route('/convertMd2Html', methods=['POST'])
def convertMd2Html():
    
    markdown_txt = request.form['text']
    # print("I'm clicked", markdown)
    html = markdown.markdown(markdown_txt)
    return jsonify({'html': html})
    # return jsonify({'name': name, 'list':html})

@app.route('/launch')
def launch_script():
    parameter = request.args.get('param')
    # Call your Python function (function1) with the provided parameter
    querry = function1(parameter)
    result = render_markdown_file('markdown/ReadMe.md')
    # save the result to a html file
    with open('../templates/markdown.html', 'w') as f:
        f.write(result)
    return querry

def function1(parameter):
    # Scrape the repo
    extractor(parameter, 'data/parameters.json', 'data/paths.json', 'data/data.json')
    querry = prompt_engine()
    return querry

def render_markdown_file(file_path):
    with open(file_path, 'r') as file:
        markdown_content = file.read()
        html_content = markdown.markdown(markdown_content, extensions=['markdown.extensions.extra', 'markdown.extensions.nl2br'])
        return html_content

if __name__ == '__main__':
    app.run(debug=False)