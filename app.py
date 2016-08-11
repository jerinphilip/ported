from wsmeext.flask import signature

import flask
import pkg_resources

def unpack(data):
    print(data)
    func = data[0]
    args = data[1:-1]
    rettype = data[-1]
    return (func, args, rettype)

def main():
    app = flask.Flask(__name__)
    app.config['DEBUG'] = True
    for entrypoint in pkg_resources.iter_entry_points('libindic.api.rest'):
        print(entrypoint.load()())
        func, args, rettype = unpack(entrypoint.load()())
        app.route('/' + func.__name__, methods=['POST', 'GET'])(
        signature(rettype, *args)(func))
    app.run()

if __name__ == '__main__':
    main()

