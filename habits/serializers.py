from rest_framework import serializers, viewsets

from .models import Habit

class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = 'all'
