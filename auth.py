from eve.auth import BasicAuth, TokenAuth
from flask import current_app


class MyBasicAuth(BasicAuth):  
    def check_auth(self, username, password, allowed_roles, resource,
                   method):
        if resource == 'account_login':
            accounts = current_app.data.driver.db['accounts']
            user = accounts.find_one({'username': username, 'password': password})
            if method == 'GET':
                if user and '_id' in user:
                    self.set_request_auth_value(user['username'])
                    return user

class MyTokenAuth(TokenAuth):
    def check_auth(self, token, allowed_roles, resource, method):
        accounts = current_app.data.driver.db['accounts']
        user = accounts.find_one({'token': token})
        if resource == 'expense':
            if method == 'GET':
                if user and '_id' in user:
                    self.set_request_auth_value(user['username'])
                    return user
            elif method == 'POST':
                    return True         
        elif resource == 'account_login':
            if method == 'POST':
                return True
    
