from wsgiref.validate import validator
from django.forms import ValidationError
from rest_framework import serializers
from .models  import Student


#validators
def start_with_d(value):
   
    if value[0].lower() != 'd':
        raise serializers.ValidationError("name must be start with 'd' ")

class StudentSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    name = serializers.CharField(max_length=100, validators=[start_with_d])
    role = serializers.IntegerField()


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        # instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.role = validated_data.get('role', instance.role)
        instance.save()
        return instance



    def validate_role(self, attrs):
        if attrs >= 150:
            raise serializers.ValidationError('seats are full!!!! ')
        return attrs

    def validate(self, attrs):
        
        name=attrs.get('name')
        role=attrs.get('role')
        if name.lower() == "demon" and role != 1:
            raise serializers.ValidationError('please enter correct role no.')
        
        return attrs

