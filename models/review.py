#!/usr/bin/env python3
"""Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """class review inheriting from baseModel
    """

    place_id = ""
    user_id = ""
    text = ""
