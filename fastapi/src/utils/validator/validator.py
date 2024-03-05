from src.utils.validator.exceptions import AppValidationException
from src.api.payloads.base import BasePayload


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

    def validated(self):
        """Validates the data and throws exception if data is not valid else returns validated data"""
        self.validate()
        if self.dto is None:
            return self.validated_data
        return self.dto.init(**self.validated_data)

    def _validate(self):
        if self.is_validated:
            pass

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
                next_rule_error = check_function(self.data, field, title=custom_title, *args)

                if next_rule_error:
                    next_field_errors.append(next_rule_error)

            if len(next_field_errors) > 0:
                self.errors[field] = next_field_errors
            else:
                # TODO: TEST
                if field in self.data:
                    self.validated_data[field] = self.data[field]

        self.is_validated = True

    def _parse_rule(self, rule, separator=":", kwargs_separator=","):
        kwargs = None
        if separator in rule:
            rule, kwargs = rule.split(separator)
            kwargs = kwargs.split(kwargs_separator)
        return rule, kwargs


class Rules:
    REQUIRED = 'required'
    NULLABLE = 'nullable'
    INTEGER = 'integer'
    FLOAT = 'float'
    STRING = 'string'
    LIST = 'list'
    FIELDS_OR = 'fields_or'

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

    @staticmethod
    def fields_or(data: dict, key: str, title: str = None, *fields: list):
        fields = [key, *fields]
        for field in fields:
            if field in data and data[field] is not None:
                return None

        return f"One of fields {', '.join(fields)} must be present."  # todo deal with title (pass titles 4 all fields somehow)
