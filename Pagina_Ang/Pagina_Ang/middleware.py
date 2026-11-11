from django.db import DatabaseError, OperationalError
from django.http import JsonResponse


class DatabaseErrorJsonMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
        except (DatabaseError, OperationalError) as exc:
            return JsonResponse(
                {
                    'error': 'No se pudo acceder a la base de datos',
                    'detalle': str(exc),
                    'status': 503,
                },
                status=503,
            )
