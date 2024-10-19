from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .serializers import HabitSerializer


class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# Публичные привычки
class PublicHabitViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)