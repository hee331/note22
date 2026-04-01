from rest_framework import serializers
from models import data


class DataSerializer(serializers.Serializer):
    class Meta:
        model = data
        fields = '__all__'


class AccountSerializer(serializers.Serializer):

    def create(self, validated_data):
        return data.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.hobbies = validated_data.get('hobbies', instance.hobbies)
        instance.gakureki = validated_data.get('gakureki', instance.gakureki)
        instance.save()
        return instance


