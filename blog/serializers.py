from rest_framework import serializers
from .models import blogs

class blogsSerializers(serializers.ModelSerializer):

     class Meta:
         model=blogs
         #fields
         fields='__all__'
