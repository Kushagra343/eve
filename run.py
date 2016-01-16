from eve import Eve
from eve.auth import BasicAuth


class MyBasicAuth(BasicAuth):

    def check_auth(self, username, password, allowed_roles, resource, method):
        return username == 'kush' and password == '1234'


app = Eve(auth=MyBasicAuth)
app.run()
