from wsmeext.flask import signature
import json

import flask
import pkg_resources

functions = {}
app = flask.Flask(__name__)
app.config['DEBUG'] = True

def unpack(data):
    func = data[0]
    args = data[1:-1]
    rettype = data[-1]
    return (func, args, rettype)

@app.route('/')
def index():
    return flask.jsonify(**functions)

def main():
    for entrypoint in pkg_resources.iter_entry_points('libindic.api.rest'):
        func, args, rettype = unpack(entrypoint.load()())
        module, fname = func.__name__.split('_')
        if module in functions:
            functions[module].append(fname)
        else:
            functions[module] = [fname]
            
        fname = func.__name__.replace('_', '/')
        app.route('/' + fname, methods=['POST', 'GET'])(
        signature(rettype, *args)(func))


if __name__ == '__main__':
    main()
    app.run()

