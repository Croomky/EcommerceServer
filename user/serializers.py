from .models import Profile
from rest_framework import serializers


class ProfileSerializer(serializers.Serializer):
    first_name = serializers.CharField(
        source="get_first_name"
    )
    last_name = serializers.CharField(
        source="get_last_name"
    )
    email = serializers.CharField(
        source="get_email"
    )

    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'email',
            'country',
            'region',
            'city',
            'post_code',
            'address_line_1',
            'address_line_2',
            'phone_number'
        )