from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from .user_account import UserAccount


class DesiredRequiredSaving(models.Model):
    required = models.IntegerField(default=0)
    nonrequired = models.IntegerField(default=0)
    saving = models.IntegerField(default=0)
    loans = models.IntegerField(default=0)
    contribution = models.IntegerField(default=0)
    other = models.IntegerField(default=0)
    user = models.OneToOneField(
        UserAccount, on_delete=models.CASCADE, related_name="saving"
    )

    class Meta:
        app_label = "account"

    def __str__(self):
        return f"{self.user}'s Desired Required Savings"


@receiver(post_save, sender=UserAccount)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        DesiredRequiredSaving.objects.create(user=instance)
