from dataclasses import fields
from rest_framework import serializers

from .models import Movie, StreamPlatform, Review

# ----------------------------------- Model Serializer -----------------------------------


class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class MovieSerializer(serializers.ModelSerializer):
    len_title = serializers.SerializerMethodField()
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        # Include fields
        fields = "__all__"
        # Exclude fields
        # exclude = ['name_of_excluded_field', ...]

    def get_len_title(self, object):
        return len(object.title)


class StreamPlatformSerializer(serializers.ModelSerializer):
    # Relation as nested object
    movies = MovieSerializer(many=True, read_only=True)
    # Relation as string representation
    # movies = serializers.StringRelatedField(many=True)
    # Relation as object primary key
    # movies = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # Relation as object hyperlink
    # movies = serializers.HyperlinkedRelatedField(
    #    many=True, read_only=True, view_name='movie-details')

    class Meta:
        model = StreamPlatform
        fields = "__all__"


"""
# ----------------------------------- Generic Serializer -----------------------------------
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
"""
