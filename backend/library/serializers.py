from rest_framework import serializers
from .models import LibraryCard


class LibraryCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = LibraryCard
        fields = [
            'id',
            'student',
            'card_number',
            'issue_date',
            'expiry_date',
        ]