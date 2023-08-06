from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .user_account import UserAccount


class Income(models.Model):
    wage_after_taxes = models.CharField(max_length=30)
    other_income = models.CharField(max_length=30)
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, related_name="income"
    )

    class Meta:
        app_label = "account"

    def __str__(self):
        return f"{self.user}'s income"


@receiver(post_save, sender=UserAccount)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Income.objects.create(user=instance)
