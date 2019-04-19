from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = (
            "first_name",
            "last_name",
            "email",
            "country",
            "region",
            "city",
            "post_code",
            "address_line_1",
            "address_line_2",
            "phone_number",
        )

    first_name = serializers.CharField(source="get_first_name")
    last_name = serializers.CharField(source="get_last_name")
    email = serializers.CharField(source="get_email")
    country = serializers.CharField(source="get_country")
    region = serializers.CharField(source="get_region")
    city = serializers.CharField(source="get_city")
    post_code = serializers.CharField(source="get_post_code")
    address_line_1 = serializers.CharField(source="get_address_line_1")
    address_line_2 = serializers.CharField(source="get_address_line_2")
    phone_number = serializers.CharField(source="get_phone_number")
