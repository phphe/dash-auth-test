import dash_auth
import base64
import flask

class CustomBasicAuth(dash_auth.BasicAuth):
    def __init__(self, app, authenticate):
        dash_auth.BasicAuth.__init__(self, app, [])
        self.authenticate = authenticate
    def is_authorized(self):
        header = flask.request.headers.get('Authorization', None)
        if not header:
            return False
        username_password = base64.b64decode(header.split('Basic ')[1])
        username_password_utf8 = username_password.decode('utf-8')
        username, password = username_password_utf8.split(':')
        return self.authenticate(username, password)
