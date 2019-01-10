
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, CCS!'

    input = request.args.get('search-term')
    print(input)

    open file for reading, 'r'
        file is saved to variable
        index_file = open('index.html', 'r')
        read contents of the index_file
        my_html = my_html.replace("{{search-term-value}}",input)

