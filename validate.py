#cerberus  is a Python validation library
from cerberus import Validator
valid = Validator()
valid.schema = {"contact_details": {
    "type": "dict",
    "schema": {
        "phone": {
            "type": "string",
            "minlength": 10,
            "maxlength": 10,
            "regex": "^0[0-9]{9}$"
        },
        "email": {
            "type": "string",
            "minlength": 8,
            "maxlength": 255,
            "required": True,
            "regex": "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$"
        }
    }
}}

if valid.validate({'contact_details': {'phone': '0781992878',
                                   'email': 'niyodusengamussa@gmail.com'}}):
    print('date is valid')
else:
    print('invalid data')
    print(valid.errors)