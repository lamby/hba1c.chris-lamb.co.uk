import json
import functools

from django.http import HttpResponse, HttpResponseBadRequest

class ajax(object):
    def __init__(self, required=True):
        self.required = required

    def allow_request(self, request):
        if not self.required:
            return True

        if request.user.is_superuser:
            return True

        if request.META.get('SERVER_NAME') == 'testserver':
            return True

        if request.is_ajax():
            return True

        return False

    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapped(request, *args, **kwargs):
            if not self.allow_request(request):
                return HttpResponseBadRequest()

            response = fn(request, *args, **kwargs) or {}

            if isinstance(response, dict):
                return HttpResponse(
                    json.dumps(response),
                    content_type='text/html' if request.FILES else 'application/json',
                )

            return response
        return wrapped

class jsonp(object):
    def __call__(self, fn):
        @functools.wraps(fn)
        def wrapped(request, *args, **kwargs):
            response = fn(request, *args, **kwargs) or {}

            if not isinstance(response, dict):
                return response

            val = json.dumps(response)
            callback = request.GET.get('callback', '')

            if callback:
                val = u'%s(%s)' % (callback, val)

            return HttpResponse(val, content_type='application/javascript')

        return wrapped
