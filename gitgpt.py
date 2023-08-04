from flask import Flask, render_template, url_for, request, jsonify
from repo_extractor_html import extractor_html
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/handle_form', methods=['POST'])
def handle_form():
    repo_name = request.form['name']
    html = extractor_html()
    print(repo_name)
    return jsonify({'list':html})

@app.route('/generateReadme', methods=['POST'])
def generateReadme():
    print("I'm clicked")
    markdown = "Hell I'm a mark down"
    return jsonify({'md': markdown})
    # return jsonify({'name': name, 'list':html})
if __name__ == '__main__':
    app.run()