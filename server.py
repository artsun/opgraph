# encoding: utf-8

import json
from flask import Flask, request, render_template

from opengraph import OpenGraph

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'
}

app = Flask(__name__)

# http://localhost:5000/?url=https://moz.com/blog/meta-data-templates-123
# http://localhost:5000/?url=https://tproger.ru/articles/dealing-with-cyber-crime/


@app.route('/', methods=['GET'])
def index():
    """
    обработка REST-запроса GET
    """
    if request.method == 'GET' and request.args.get('url'):
        url = request.args.get('url')
        res = json.dumps(OpenGraph(url, HEADERS), ensure_ascii=False)
    else:
        res = 'Incorrect request. Try: url=https://...'

    return render_template('index.html', data=res)

@app.errorhandler(404)
def page_not_found(*args):
    """
    обработка случая: страница не найдена
    """
    return render_template('index.html', data='Incorrect request. Try: url=https://...'), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=False)
