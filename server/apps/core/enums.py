from enum import Enum


class DjangoChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def values(cls):
        return tuple(i.value for i in cls)

    @classmethod
    def has_value(cls, item):
        return item in [v.value for v in cls.__members__.values()]
