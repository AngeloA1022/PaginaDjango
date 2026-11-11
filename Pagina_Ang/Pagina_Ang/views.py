from django.shortcuts import render


def error_db_view(request, exception=None):
    return render(request, 'error_db.html', status=503)


def error_404_view(request, exception=None):
    return render(request, 'error_db.html', status=404)
