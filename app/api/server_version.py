from flask import jsonify, Blueprint

SERVER_VERSION = '1.11.1'

info_route = Blueprint('info', __name__)
_build = {'version': SERVER_VERSION}


@info_route.route('/info')
def version():
    return jsonify(build=_build)
