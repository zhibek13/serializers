from rest_framework import serializers
from .models import Position, Employee


class PositionSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.department = validated_data.get('department')
        instance.save()
        return instance


class EmployeeSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    birth_date = serializers.CharField(max_length=30)
    position = serializers.CharField(max_length=100)
    salary = serializers.IntegerField()

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.birth_date = validated_data.get('birth_date')
        instance.position = validated_data.get('position')
        instance.salary = validated_data.get('salary')
        instance.save()
        return instance

