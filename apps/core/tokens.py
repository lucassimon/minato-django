from django.conf import settings
from django.utils.functional import cached_property

from rest_framework_simplejwt.tokens import UntypedToken
from rest_framework_simplejwt.models import TokenUser
from rest_framework_simplejwt.compat import CallableFalse, CallableTrue
from rest_framework_simplejwt.settings import api_settings


class BearerToken(UntypedToken):
    lifetime = settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]


class CustomTokenUser(TokenUser):
    @cached_property
    def id(self):
        return self.token[api_settings.USER_ID_CLAIM]["user"]["id"]

    @cached_property
    def profile_id(self):
        return self.token[api_settings.USER_ID_CLAIM]["user"]["profile_id"]

    @cached_property
    def identity_id(self):
        return self.token[api_settings.USER_ID_CLAIM]["user"]["identity_id"]

    @cached_property
    def pk(self):
        return self.id

    @cached_property
    def email(self):
        return self.token[api_settings.USER_ID_CLAIM]["user"]["email"]

    def get_email(self):
        return self.email


# token = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjJhMjFmZWY1LTQ5NjQtNGJjYi04ZTZlLTliMTVmZWQ4NGE1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2MzA1MjU4MTUsImlhdCI6MTYzMDM1MzAxNSwiaXNzIjoiaHR0cDovL2xvY2FsLmFwcC5wcmV2ZXIuY29tIiwianRpIjoiZmI2OTExMWEtNjkwOS00MGY3LTg0YmYtOGFiZTgxZTkwNjcxIiwibmJmIjoxNjMwMzUzMDE1LCJzZXNzaW9uIjp7InVzZXIiOnsiZW1haWwiOiJ0ZXN0ZTMzQGdtYWlsLmNvbSIsImlkIjoyLCJpZGVudGl0eSI6eyJpZCI6ImUzOGFkZWI1LWQ3MmYtNDI1Ni1iYTAzLWE3NzE5M2FiZWMyNiJ9LCJpZGVudGl0eV9pZCI6ImUzOGFkZWI1LWQ3MmYtNDI1Ni1iYTAzLWE3NzE5M2FiZWMyNiIsInByb2ZpbGVfaWQiOiIyMSJ9fSwic3ViIjoiIn0.OlxKIFq-6wMWByxj28ArXp3gPfvCucdM_jdxEiH4zOEKrcA2S_KyUG1vY7G7VDVP7w-LmxV2BcYvrpWH_xdQX7exWoiN7xRXK5fop8fbzSRc5VGYWgjwlXmTRf9FVTHRoQU6T1rYo9_4Q8XFvtDNGxb538haJBuoAR5lBVWhlkAF0FYSWDERxUVFJVtfmXjgdza_fw4kK3-zhhYxANV3njApYGI9IgeSgogfR10bu52DY6PAF9-Tbpx3RlCl6vGY5SYjvJdc9_ChyJJ0ZhSsBac4jrASBJwtGpqaQuoyiowCrMScWdyIcUNyALZT2ymFcu6nbrfdCtraCeRGihil2g"
