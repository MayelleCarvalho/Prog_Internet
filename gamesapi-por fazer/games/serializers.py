from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Game


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ('id', 'name', 'release_date', 'game_category')
        validators = [
            UniqueTogetherValidator(
                queryset=Game.objects.all(),
                message = 'O campo nome não pode ser repetido',
                fields=('name', 'name')
            )
        ]