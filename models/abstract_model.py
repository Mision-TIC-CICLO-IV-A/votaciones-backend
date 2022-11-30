from abc import ABCMeta


class AbstractModel(metaclass=ABCMeta):

    def __init__(self, data: dict):
        """
        This method is a constructor where a dict is used to define current class attributes
        :param data:
        """
        for key, value in data.items():
            setattr(self, key, value)
