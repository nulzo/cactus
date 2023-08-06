from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .user_account import UserAccount


class DesiredNonrequiredSpending(models.Model):
    clothing = models.IntegerField(default=0)
    eating_out = models.IntegerField(default=0)
    alcohol = models.IntegerField(default=0)
    events = models.IntegerField(default=0)
    travel = models.IntegerField(default=0)
    recurring_app_payments = models.IntegerField(default=0)
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, related_name="nonreq"
    )

    class Meta:
        app_label = "account"

    def __str__(self):
        return f"{self.user}'s Desired Non-Required Spending"


@receiver(post_save, sender=UserAccount)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        DesiredNonrequiredSpending.objects.create(user=instance)
