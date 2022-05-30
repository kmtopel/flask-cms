from flask import render_template
from . import app

example_blocks = [
    {
        "id":"1",
        "name": "Banner",
        "content": "Lorem Ipsum "
    },
    {
        "id":"2",
        "name": "Paragraph",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    },
    {
        "id":"3",
        "name": "Image",
        "content": "test"
    }
]

@app.route('/')
def index():
    return render_template('index.html', blocks=example_blocks)