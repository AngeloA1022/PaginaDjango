from django.db import DatabaseError, InterfaceError, OperationalError
from django.shortcuts import render

from Pagina_Ang.datos_offline import guardar_datos_offline


class DatabaseErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if isinstance(exception, (DatabaseError, OperationalError, InterfaceError)):
            datos = request.POST.dict() if request.method == 'POST' else {}
            guardar_datos_offline('error_base_de_datos', datos)
            return render(request, 'error_db.html', status=503)
        return None
