from rest_framework import serializers

from accounts.models import Account


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'owner', 'balance', 'creation_date')

    def validate_balance(self, value):

        if value < 0:
            raise serializers.ValidationError("O valor do balance não pode ser negativo")
        return value

    def validate_data(self, value):

        if value != None:
            raise serializers.ValidationError("O campo data é automático")
        return value

