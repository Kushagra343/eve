from eve import Eve
from auth import MyBasicAuth, MyTokenAuth


DOMAIN = {
    'account_login': {
        'url': 'login',
        'datasource': {
            'source': 'accounts',
            'projection': {'token':1},
        },
        "extra_response_context": ["token"],
        "authentication": MyTokenAuth,
        'resource_methods': ['GET', 'POST'],
        'item_methods': ['GET', 'PUT'],
        'auth_field': 'username',

        'schema': {
            'username': {
                'type': 'string',
                'minlength': 6,
                'maxlength': 10,
                'required': True,
                'unique': True,
            },
            'password': {
                'type': 'string',
                'minlength': 6,
                'maxlength': 10,
                'required': True,
            },
            'phone': {
                'type': 'integer',
                'minlength': 10,
                'maxlength': 10,
                'required': True,
            },
            'organization': {
                'type': 'string',
                'minlength': 6,
                'maxlength': 20,
                'required': True,
            },

        },

        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username',
        },
    },

    'expense': {
        'url': 'expense',
        'datasource': {
            'source': 'expense',
        },
        "authentication": MyTokenAuth,
        'resource_methods': ['GET', 'POST'],
        'item_methods': ['GET', 'PUT'],
        'auth_field': 'username',
        'schema': {
            'username': {
                'type': 'string',
                'minlength': 6,
                'maxlength': 10,
                'required': True,
             },
            "amount": {
                "type": "integer",
                "required": True
            },

            "description": {
                "type": "string",
                "maxlength": 500
            },

            "pictures": {},

            "location": {
                "type": "point",
            },

            "tags": {
                "type": "list",
            },
        },

        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': '_id',
        },
    },

}



EVE_SETTINGS = {
    "RESOURCE_METHODS": ['GET', 'POST', 'DELETE'],
    "ITEM_METHODS": ['GET', 'PATCH', 'DELETE'],
    "DOMAIN": DOMAIN,
    "MONGO_HOST": "localhost",
    "MONGO_POST": "27017",
    "MONGO_DBNAME": "expense",
    "DATE_CREATED": "created_at",
    "LAST_UPDATED": "updated_at",
    "XML": True,
    "X_DOMAINS": '*',
    "X_ALLOW_CREDENTIALS": True,
    "X_HEADERS": ['Authorization', 'Content-Type'],
}

def add_token(documents):
    for document in documents:
        payload = {'username': document['username']}
        document["token"] = 'hello'    

if __name__ == '__main__':
    app = Eve(settings=EVE_SETTINGS)
    app.on_insert_account_login += add_token
    app.run()


