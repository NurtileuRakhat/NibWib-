import django
from django.utils.encoding import smart_str
from django.utils.translation import gettext

django.utils.encoding.smart_text = smart_str # fix deprecated import
django.utils.translation.ugettext = gettext # fix deprecated import
from rest_framework_jwt.authentication import JSONWebTokenAuthentication  # noqa


class CustomJSONWebTokenAuthentication(JSONWebTokenAuthentication):
    def authenticate(self, request):
        print("Request received:", request)
        tuple_response = super(CustomJSONWebTokenAuthentication, self).authenticate(request)
        print("Tuple response:", tuple_response)
        return tuple_response

    def authenticate_credentials(self, payload):
        print("Payload received:", payload)
        user = super(CustomJSONWebTokenAuthentication, self).authenticate_credentials(payload)
        print("User:", user)
        return user
