MONGO_HOST = 'LOCALHOST'
MONGO_PORT = 27017
MONGO_USERNAME = ''
MONGO_PASSWORD = ''
MONGO_DBNAME = 'apitest'
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
RESOURCE_ITEMS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 10,
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 15,
        'required': True,
        'unique': True,
    },
    'role': {
        'type': 'list',
        'allowed': ["author", "contributor", "copy"],
    },
    'location': {
        'type': 'dict',
        'schema': {
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'born': {
        'type': 'datetime',
    },
}

people = {
    'item_title': 'person',
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'lastname'
    },
    'resource_methods': ['GET', 'POST'],
    'schema': schema
}

DOMAIN = {'people': people, }
