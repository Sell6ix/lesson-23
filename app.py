
import ast
import os
from flask import Flask, request, jsonify
from class_query import Query

app = Flask(__name__)


@app.route('/perform_query', methods=['GET', 'POST'])
def post():
    req = json.loads(request.data)
    path = os.path.abspath(f'data/{req["file_name"]}')

    with open(path, 'r', encoding='utf-8') as file:
        method = getattr(Query, req['cmd1'], "Такого метода нет")
        result = method(req['value1'], file)
        if 'cmd2' in req:
            method2 = getattr(Query, req['cmd2'], "Такого метода нет")
            result = method2(req['value2'], result)
        return jsonify(list(result))


if __name__ == '__main__':
    app.run()
