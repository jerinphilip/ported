from wsmeext.flask import signature

import flask
import pkg_resources


def main():
    app = flask.Flask(__name__)
    app.config['DEBUG'] = True
    for entrypoint in pkg_resources.iter_entry_points('libindic.api.rest'):
    #for entrypoint in pkg_resources.iter_entry_points('myapp.api.rest'):
        func, *args, rettype = entrypoint.load()()
        print(func.__name__, rettype, args)
        app.route('/' + func.__name__, methods=['POST', 'GET'])(
        signature(rettype, *args)(func))
        #app.route('/' + func.__name__, methods=['GET'])(
                
        #        )
    app.run()

if __name__ == '__main__':
    main()

