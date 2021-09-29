from rest_framework import serializers
from .models import Shortener

class urlSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shortener
        fields=['id','created','times_followed','long_url','short_url']
