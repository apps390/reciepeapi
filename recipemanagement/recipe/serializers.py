from rest_framework import serializers
from recipe.models import recipe, review
from django.contrib.auth.models import User


class reciepeserializers(serializers.ModelSerializer):
    class Meta:
        model = recipe
        fields = ['id','recipe_name','recipe_ingredients','instructions','cuisine','meal_type','created','updated']


class userserializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username', 'password']

    def create(self, validated_user):
        user = User.objects.create_user(username=validated_user['username'], password=validated_user['password'])
        user.save()
        return user


class reviewserializers(serializers.ModelSerializer):
    class Meta:
        model = review
        fields='__all__'
