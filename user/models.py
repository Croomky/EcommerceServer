from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=200, blank=True)
    region = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    post_code = models.CharField(max_length=15, blank=True)
    address_line_1 = models.CharField(max_length=200, blank=True)
    address_line_2 = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=200, blank=True)

    def get_first_name(self):
        return self.user.first_name

    def get_last_name(self):
        return self.user.last_name

    def get_email(self):
        return self.user.email

    def get_country(self):
        return self.country

    def get_region(self):
        return self.region

    def get_city(self):
        return self.city

    def get_post_code(self):
        return self.post_code

    def get_address_line_1(self):
        return self.address_line_1

    def get_address_line_2(self):
        return self.address_line_2

    def get_phone_number(self):
        return self.phone_number
