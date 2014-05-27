"""
Serialize data to/from JSON

Django now uses standard library json and breaks if you use simplejson.
"""
from __future__ import absolute_import

import json

from django.utils import simplejson
from .python import Serializer as PythonSerializer
from django.core.serializers.json import Deserializer as JSONDeserializer, \
    DjangoJSONEncoder

class Serializer(PythonSerializer):
    """
    Convert a queryset to JSON.
    """
    def end_serialization(self):
        """Output a JSON encoded queryset."""
        json.dump(self.objects, self.stream, cls=DjangoJSONEncoder,
            **self.options)

    def getvalue(self):
        """
        Return the fully serialized queryset (or None if the output stream
        is not seekable).
        """

        if callable(getattr(self.stream, 'getvalue', None)):
            return self.stream.getvalue()

Deserializer = JSONDeserializer
