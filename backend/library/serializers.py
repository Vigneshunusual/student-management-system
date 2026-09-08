from rest_framework import serializers
from .models import LibraryCard


class LibraryCardSerializer(serializers.ModelSerializer):
    
    def validate(self, attrs):
        issue_date = attrs.get('issue_date')
        expiry_date = attrs.get('expiry_date')

        if issue_date and expiry_date and expiry_date < issue_date:
            raise serializers.ValidationError({
                'expiry_date': 'Expiry date cannot be before issue date.'
            })

        return attrs
    class Meta:
        model = LibraryCard
        fields = [
            'id',
            'student',
            'card_number',
            'issue_date',
            'expiry_date',
        ]