import re


class DataValidator:

    @staticmethod
    def is_null(val):
        if (val == ''):
            return True
        else:
            False

    @staticmethod
    def is_not_null(val):
        if val == None or val == "":
            return False
        else:
            return True

    @classmethod
    def is_email(self, val):
        if re.match("[^@]+@[^@]+\.[^@]+", val):
            return True
        else:
            return False

    @classmethod
    def is_alphabet(self, val):
        if re.match("^[a-zA-z\s]+$", val):
            return True
        else:
            return False
