from rest_framework import serializers

from .models import Movie

# Defined custom field level validator


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short!")


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

    # Field-level validation
    # def validate_name(self, value):
    #     if len(value) < 2:
    #         raise serializers.ValidationError("Name is too short!")
    #     else:
    #         return value

    # Object-level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError(
                'Name and Description should not be the same!')
        else:
            return data
