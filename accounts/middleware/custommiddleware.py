from django.contrib.auth.hashers import check_password
from django.http import HttpResponseForbidden
from ..models import Vendor

class VendorAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
    def authenticate_vendor(self, request, email, password):
        try:
            user = Vendor.objects.get(email=email)
            if check_password(password, user.password):
                request.vendor = user
                vendor_data = {
                    'id': user.id,
                    'name': user.name,
                    'email': user.email,
                    'password': user.password,
                    'phone': user.phone,
                    # Add other attributes you want to store
                }
                request.session['vendor_user'] = vendor_data
    
                return user
        except Vendor.DoesNotExist:
            pass
        return None
