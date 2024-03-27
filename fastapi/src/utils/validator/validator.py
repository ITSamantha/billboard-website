import datetime

from src.utils.validator.exceptions import AppValidationException
from src.api.payloads.base import BasePayload
import re


class Validator:

    def __init__(self, data: dict, rules: dict, titles: dict = {}, dto: BasePayload = None):
        self.data = data
        self.rules = rules
        self.titles = titles
        self.dto = dto

        self.is_validated = False

        self.errors = {}
        self.validated_data = {}

    def validate(self):
        """Validates the data and throws exception if data is not valid"""
        self._validate()
        if self.errors:
            raise AppValidationException(errors=self.errors)

    def get_errors(self) -> dict:
        """Validates the data and returns dict with errors if data is not valid"""
        self._validate()
        return self.errors

    def validated(self, as_dict: bool = False):
        """Validates the data and throws exception if data is not valid else returns validated data"""
        self.validate()
        if self.dto is None or as_dict:
            return self.validated_data
        return self.dto.init(**self.validated_data)

    def only(self, keys: list[str]) -> dict:
        """Returns specified fields as dict"""
        print(self.validated(as_dict=True))
        return {key: value for key, value in self.validated(as_dict=True).items() if key in keys}

    def all(self) -> dict:
        """Returns all fields as dict"""
        return self.validated(as_dict=True)

    def not_null(self) -> dict:
        """Returns all fields as dict"""
        return {key: value for key, value in self.validated(as_dict=True).items() if value is not None}

    def but(self, keys: list[str]) -> dict:
        """Returns all fields except specified as dict"""
        return {key: value for key, value in self.validated(as_dict=True).items() if key not in keys}

    def but__not_null(self, keys: list[str]) -> dict:
        """Returns all fields except specified as dict"""
        return {key: value for key, value in self.validated(as_dict=True).items() if
                key not in keys and value is not None}

    def _validate(self):
        if self.is_validated:
            return

        rules_checker = Rules()
        for field in self.rules:
            try:
                rules = self.rules[field]
            except KeyError:
                continue

            if not isinstance(rules, list):
                raise Exception('Rules must be of type list')  # todo custom?

            next_field_errors = []

            for rule in rules:
                try:
                    rule, args = self._parse_rule(rule)
                    check_function = getattr(rules_checker, rule)
                except AttributeError:
                    raise Exception(f'Rule {rule} is not defined')  # todo custom?

                custom_title = self.titles[field] if field in self.titles else None
                next_rule_error = check_function(self.data, field, custom_title, *args)

                if next_rule_error:
                    next_field_errors.append(next_rule_error)

            if len(next_field_errors) > 0:
                self.errors[field] = next_field_errors
            else:
                # TODO: TEST
                if field in self.data:
                    self.validated_data[field] = self.data[field]

        self.is_validated = True

    def _parse_rule(self, rule, separator=":", args_separator=","):
        args = []
        if separator in rule:
            rule, args = rule.split(separator)
            args = args.split(args_separator)
        return rule, args


class Rules:
    REQUIRED = 'required'
    NULLABLE = 'nullable'
    INTEGER = 'integer'
    FLOAT = 'float'
    STRING = 'string'
    LIST = 'list'
    REQUIRED_WITHOUT = 'required_without'

    @staticmethod
    def required(data: dict, key: str, title: str = None):
        if key in data and data[key] is not None:
            return None

        return f"{title if title else key} is required."

    @staticmethod
    def nullable(data: dict, key: str, title: str = None):
        if key in data:
            return None

        return f"{title if title else key} must be present."

    @staticmethod
    def integer(data: dict, key: str, title: str = None):
        if key in data and not isinstance(data[key], (int, type(None))):
            return f"{title if title else key} field must be of type integer."

        return None

    @staticmethod
    def bool(data: dict, key: str, title: str = None):
        if key in data and not isinstance(data[key], (bool, type(None))):
            return f"{title if title else key} field must be of type integer."

        return None

    @staticmethod
    def float(data: dict, key: str, title: str = None):
        if key in data and not (isinstance(data[key], (float, type(None))) or isinstance(data[key], (int, type(None)))):
            return f"{title if title else key} field must be of type float."

        return None

    @staticmethod
    def string(data: dict, key: str, title: str = None):
        if key in data and not isinstance(data[key], (str, type(None))):
            return f"{title if title else key} field must be of type string."

        return None

    @staticmethod
    def list(data: dict, key: str, title: str = None):
        if key in data and not isinstance(data[key], (list, type(None))):
            return f"{title if title else key} field must of type list."

        return None
    """
    @staticmethod
    def datetime(data: dict, key: str, title: str = None):
        if key in data and not isinstance(data[key], (datetime.datetime, type(None))):
            return f"{title if title else key} field must be of type datetime."

        return None
    """

    @staticmethod
    def required_without(data: dict, key: str, title: str = None, *fields: list):
        fields = [key, *fields]
        for field in fields:
            if field in data and data[field] is not None:
                return None

        return f"One of fields {', '.join(fields)} must be present."  # todo deal with title (pass titles 4 all fields somehow)

    @staticmethod
    def email(data: dict, key: str, title: str = None):
        if key in data and not re.fullmatch(
                re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'),
                str(data[key])
        ):
            return f"{title if title else key} field must a valid email."
        return None
