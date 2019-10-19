"""Quart plugin

Heavily copied from apispec
"""

from collections.abc import Mapping
import re

import quart.routing

from apispec import BasePlugin


# from flask-restplus
RE_URL = re.compile(r'<(?:[^:<>]+:)?([^<>]+)>')

# From flask-apispec
DEFAULT_CONVERTER_MAPPING = {
    quart.routing.StringConverter: ('string', None),
    quart.routing.IntegerConverter: ('integer', 'int32'),
    quart.routing.FloatConverter: ('number', 'float'),
    quart.routing.UUIDConverter: ('string', 'uuid'),
}
DEFAULT_TYPE = ('string', None)


class QuartPlugin(BasePlugin):
    """Plugin to create OpenAPI paths from Quart rules"""

    def __init__(self):
        super().__init__()
        self.converter_mapping = dict(DEFAULT_CONVERTER_MAPPING)
        self.openapi_version = None

    def init_spec(self, spec):
        super().init_spec(spec)
        self.openapi_version = spec.openapi_version

    # From apispec
    @staticmethod
    def quartpath2openapi(path):
        """Convert a Flask URL rule to an OpenAPI-compliant path.

        :param str path: Flask path template.
        """
        return RE_URL.sub(r'{\1}', path)

    def register_converter(self, converter, conv_type, conv_format=None):
        """Register custom path parameter converter

        :param BaseConverter converter: Converter.
            Subclass of werkzeug's BaseConverter
        :param str conv_type: Parameter type
        :param str conv_format: Parameter format (optional)
        """
        self.converter_mapping[converter] = (conv_type, conv_format)

    # Greatly inspired by flask-apispec
    def rule_to_params(self, rule):
        """Get parameters from flask Rule"""
        params = []
        for argument in [a for a in rule._converters.keys() if a not in rule.defaults]:
            param = {
                'in': 'path',
                'name': argument,
                'required': True,
            }
            type_, format_ = self.converter_mapping.get(
                type(rule._converters[argument]), DEFAULT_TYPE)
            schema = {'type': type_}
            if format_ is not None:
                schema['format'] = format_
            if self.openapi_version.major < 3:
                param.update(schema)
            else:
                param['schema'] = schema
            params.append(param)
        return params

    def path_helper(self, rule, operations, parameters, **kwargs):
        """Get path from flask Rule and set path parameters in operations"""

        for path_p in self.rule_to_params(rule):
            # If a parameter with same name and location is already
            # documented, update. Otherwise, append as new parameter.
            p_doc = next(
                (
                    p for p in parameters
                    if (
                        isinstance(p, Mapping) and
                        p['in'] == 'path' and
                        p['name'] == path_p['name']
                    )
                ),
                None
            )
            if p_doc is not None:
                # If parameter already documented, mutate to update doc
                # Ensure manual doc overwrites auto doc
                p_doc.update({**path_p, **p_doc})
            else:
                parameters.append(path_p)

        return self.quartpath2openapi(rule.rule)
