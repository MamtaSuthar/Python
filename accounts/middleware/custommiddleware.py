from django.contrib.auth import login as auth_login
from ..models import Vendor

class VendorAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def authenticate_vendor(self, email, password):
        try:
            user = Vendor.objects.get(email=email)
        
        except Vendor.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user  # Return the authenticated user
            return None
