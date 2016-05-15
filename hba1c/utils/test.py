from django.test import TestCase
from django.shortcuts import resolve_url

class TestCase(TestCase):
    def assertStatusCode(self, status_code, fn, to, *args, **kwargs):
        response = fn(resolve_url(to, *args, **kwargs))

        self.assertEqual(
            response.status_code,
            status_code,
            "Expected HTTP %d != saw HTTP %d. Response:\n%s" % (
                status_code,
                response.status_code,
                "%s..." % str(response)[:8000],
            ),
        )

        return response

    def assertHTTP200(self, *args, **kwargs):
        return self.assertStatusCode(200, self.client.get, *args, **kwargs)
