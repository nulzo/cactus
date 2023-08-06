from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccount(models.Model):
    phone = models.CharField(max_length=25, blank=True, unique=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        app_label = "account"
        db_table = "account"

    def __str__(self):
        return f"{self.user.username}"


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        UserAccount.objects.create(user=instance)
