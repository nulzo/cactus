from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .user_account import UserAccount


class DesiredRequiredSpending(models.Model):
    rent = models.IntegerField(default=0)
    utilities = models.IntegerField(default=0)
    groceries = models.IntegerField(default=0)
    loans = models.IntegerField(default=0)
    insurance = models.IntegerField(default=0)
    phone_bill = models.IntegerField(default=0)
    gas = models.IntegerField(default=0)
    internet = models.IntegerField(default=0)
    other = models.IntegerField(default=0)
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, related_name="req"
    )

    class Meta:
        app_label = "account"

    def __str__(self):
        return f"{self.user}'s Desired Required Spending"


@receiver(post_save, sender=UserAccount)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        DesiredRequiredSpending.objects.create(user=instance)
