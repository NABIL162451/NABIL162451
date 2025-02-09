from rest_framework import serializers
from .models import User_info,HousePost

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_info
        fields = ['Name', 'Address', 'FatherName', 'ContactNumber', 'NidNumber', 'NID']

class HousePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = HousePost
        fields = ['Area', 'Rent', 'HouseDetails', 'SquareFeet', 'PhoneNo ', 'HouseImage']
