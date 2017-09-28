import dash_auth
import base64
import flask

Auth = dash_auth.auth.Auth

class WechatAuth(Auth):
    def __init__(self, app):
        Auth.__init__(self, app)
    def is_authorized(self):
        return False
    def login_request(self):
        return '''
        <h1>login</h1>
        '''
    def auth_wrapper(self, f):
        def wrap(*args, **kwargs):
            if not self.is_authorized():
                return flask.Response(status=403)

            response = f(*args, **kwargs)
            return response
        return wrap
