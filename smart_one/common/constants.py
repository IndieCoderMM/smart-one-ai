from enum import Enum


class Status(Enum):
    ONLINE = 0
    OFFLINE = 1


class Command(Enum):
    VOICE = 0
    TEXT = 1
