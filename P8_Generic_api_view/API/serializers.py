from rest_framework import serializers
from rest_framework import validators
from .models import EmpDetails, Employee
from rest_framework.validators import ValidationError

def start_with_p(data):
    if data[0].lower()!='p':
        raise serializers.ValidationError('name should start with p')

## Serializer Class
# class EmployeeSerializer(serializers.Serializer):
#     eid=serializers.IntegerField()
#     name=serializers.CharField(max_length=32, validators=[start_with_p])
#     city=serializers.CharField(max_length=32)

#     def create(self, validated_data):
#         return Employee.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.eid=validated_data.get('eid', instance.eid)
#         instance.name=validated_data.get('name', instance.name)
#         instance.city=validated_data.get('city', instance.city)   
#         instance.save()             
#         return instance

## Model Serializer Class

class EmployeeSerializer(serializers.ModelSerializer):
    # addresses=EmpDetailsSerializer(many=True)
    class Meta:
        model=Employee
        fields=['eid', 'name', 'city', 'addresses']

class EmpDetailsSerializer(serializers.ModelSerializer):
    employee=EmployeeSerializer()
    class Meta:
        model=EmpDetails
        fields=['phone', 'state', 'employee']

# class EmployeeSerializer(serializers.ModelSerializer):
#     addresses=EmpDetailsSerializer(many=True)
#     class Meta:
#         model=Employee
#         fields=['eid', 'name', 'city', 'addresses']

    ## Field Level Validation
    def validate_eid(self, eid):
        if eid<1:
            raise ValidationError('eid can be less than zero')
        return eid

    ## Object Level Validation
    def validate(self, data):
        name=data.get('name')
        city=data.get('city')
        if name.lower()=='pratik' and city.lower()!='pune':
            raise ValidationError('city for pratik must be pune')
        return data
