import json

from common.LNG import language
from common.config import getConfig
from controller.baseController import BaseHandler, handle_request, cookieName
from service.system import userService

CONFIG = getConfig()
server = CONFIG['server']


class Login(BaseHandler):
    @handle_request
    def post(self, req):
        user = userService.checkPwd(None, req['passwd'], req['userName'])
        self.set_signed_cookie(cookieName, json.dumps(user),
                               expires_days=int(server['cookieExpiresDays']))
        userReturn = user.copy()
        del userReturn['passwd']
        del userReturn['sqlVersion']
        return userReturn

    @handle_request
    def delete(self, req):
        self.clear_cookie(cookieName)


class User(BaseHandler):
    @handle_request
    def get(self, req):
        user = req['__user']
        return user

    @handle_request
    def put(self, req):
        user = json.loads(self.get_signed_cookie(cookieName))
        userService.resetPasswd(user['id'], req['passwd'], req['oldPasswd'])


class Language(BaseHandler):
    @handle_request
    def get(self, req):
        return language()

    @handle_request
    def post(self, req):
        language(req['language'])
