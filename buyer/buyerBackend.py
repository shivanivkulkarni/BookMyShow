from django.contrib.auth.backends import ModelBackend
from buyer.models import Buyer

class BuyerBackend(ModelBackend):
    def authenticate(self, request, username, password):
        try:
            buyer = Buyer.objects.get(email=username)
            if buyer.check_password(password):
                return buyer
        except Buyer.DoesNotExist:
            return None
