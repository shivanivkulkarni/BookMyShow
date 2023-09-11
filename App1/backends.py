from django.contrib.auth.backends import ModelBackend
from seller.models import Seller
from buyer.models import Buyer

class SellerBackend(ModelBackend):
    def authenticate(self, request, username, password):
        try:
            print(username, password)
            seller = Seller.objects.get(username=username)
            print(seller)
            if seller.check_password(password):
                return seller
        except Seller.DoesNotExist:
            return None

class BuyerBackend(ModelBackend):
    def authenticate(self, request, username, password):
        try:
            buyer = Buyer.objects.get(email=username)
            if buyer.check_password(password):
                return buyer
        except Buyer.DoesNotExist:
            return None
