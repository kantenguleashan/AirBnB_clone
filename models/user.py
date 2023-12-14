#!/usr/bin/python3
""" user class moudle """

from models.base_model import BaseModel


class User(BaseModel):
    """ class user inheriting from basemodel """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
