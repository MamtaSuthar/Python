from django.conf import settings

def project_settings(request):
    return {'PROJECT': settings.PROJECT,'MEDIA_URL':settings.MEDIA_URL}
