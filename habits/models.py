from django.db import models
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    place = models.CharField(max_length=255)
    time = models.TimeField()
    action = models.CharField(max_length=255)
    is_pleasant = models.BooleanField(default=False)
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'is_pleasant': True},
        related_name='main_habits'
    )
    periodicity = models.PositiveIntegerField(default=1)  # дни по умолчанию
    reward = models.CharField(max_length=255, blank=True, null=True)
    time_to_complete = models.PositiveIntegerField()  # в секундах
    is_public = models.BooleanField(default=False)

    def clean(self):
        if self.reward and self.related_habit:
            raise ValidationError("Нельзя указать и вознаграждение, и связанную привычку одновременно.")
        if self.time_to_complete > 120:
            raise ValidationError("Время на выполнение привычки не может превышать 120 секунд.")
        if self.periodicity < 1 or self.periodicity > 7:
            raise ValidationError("Периодичность должна быть от 1 до 7 дней.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def str(self):
        return f'{self.user.email} - {self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'