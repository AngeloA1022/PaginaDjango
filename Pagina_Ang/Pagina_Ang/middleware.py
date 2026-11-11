from django.db import DatabaseError, InterfaceError, OperationalError
from django.shortcuts import render


class DatabaseErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, (DatabaseError, OperationalError, InterfaceError)):
            return render(request, 'error_db.html', status=503)
        return None
