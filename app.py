from wsmeext.flask import signature

import flask
import pkg_resources

def unpack(data):
    print(data)
    func = data[0]
    args = data[1:-1]
    rettype = data[-1]
    #func, args, rettype = data
    return (func, args, rettype)

def main():
    app = flask.Flask(__name__)
    app.config['DEBUG'] = True
    for entrypoint in pkg_resources.iter_entry_points('libindic.api.rest'):
        print(entrypoint.load()())
        func, args, rettype = unpack(entrypoint.load()())
        #print(func.__name__, rettype, args)
        app.route('/' + func.__name__, methods=['POST', 'GET'])(
        signature(rettype, *args)(func))
        #app.route('/' + func.__name__, methods=['GET'])(
                
        #        )
    app.run()

if __name__ == '__main__':
    main()

