from django.db import DatabaseError, InterfaceError, OperationalError
from django.http import HttpResponse
from django.shortcuts import render


class DatabaseErrorJsonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except (DatabaseError, OperationalError, InterfaceError):
            return render(request, 'error_db.html', status=503)
