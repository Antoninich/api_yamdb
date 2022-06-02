from enum import Enum


class Roles(Enum):
    user = 'user'
    moderator = 'moderator'
    admin = 'admin'

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
