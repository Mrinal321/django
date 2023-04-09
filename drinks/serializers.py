from rest_framework import serializers
from .models import Drink
from .models import Dog, Breed

class DogSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(slug_field='name', queryset=Breed.objects.all())

    class Meta:
        model = Dog
        fields = ('id', 'name', 'age', 'gender', 'color', 'favourite_food', 'favourite_toy', 'breed')

    # def create(self, validated_data):
    #     breed = validated_data.pop('breed')
    #     dog = Dog.objects.create(breed=breed, **validated_data)
    #     return dog
    #
    # def update(self, instance, validated_data):
    #     breed = validated_data.pop('breed')
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.age = validated_data.get('age', instance.age)
    #     instance.gender = validated_data.get('gender', instance.gender)
    #     instance.color = validated_data.get('color', instance.color)
    #     instance.favoritefood = validated_data.get('favoritefood', instance.favoritefood)
    #     instance.favoritetoy = validated_data.get('favoritetoy', instance.favoritetoy)
    #     instance.breed = breed
    #     instance.save()
    #     return instance