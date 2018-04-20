from rest_framework import serializers
from api.models import Register

class RegisterSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  email = serializers.CharField(required=True)
  password = serializers.CharField(required=True)

  def create(self, validated_data):
    return Register.objects.create(**validated_data)
  
  def update(self, instance, validated_data ):
    instance.email = validated_data.get('email', instance.email)
    instance.save()
    return instance

class RegisterSerializer2(serializers.ModelSerializer):
  
  class Meta:
    model = Register
    fields = "__all__"
    # fields = ('id', 'title', 'created_at')
