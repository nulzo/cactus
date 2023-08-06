from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

from .user_account import UserAccount


class DailySpending(models.Model):
    current_date = models.DateField(default=now)
    rent = models.IntegerField(default=0)
    utilities = models.IntegerField(default=0)
    groceries = models.IntegerField(default=0)
    loans = models.IntegerField(default=0)
    insurance = models.IntegerField(default=0)
    phone_bill = models.IntegerField(default=0)
    gas = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)
    clothing = models.IntegerField(default=0)
    eating_out = models.IntegerField(default=0)
    alcohol = models.IntegerField(default=0)
    events = models.IntegerField(default=0)
    travel = models.IntegerField(default=0)
    recurring_app_payments = models.IntegerField(default=0)
    other = models.IntegerField(default=0)
    user = models.ForeignKey(
        UserAccount, on_delete=models.CASCADE, related_name="daily"
    )

    class Meta:
        app_label = "account"

    def __str__(self):
        return f"{self.user}'s Spending on {self.current_date}"


@receiver(post_save, sender=UserAccount)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        DailySpending.objects.create(user=instance)
