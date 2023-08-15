from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


def image_path(instance):
    return f"build/profile_pictures/{instance.user.id}"


class UserAccount(models.Model):
    phone = models.CharField(max_length=25, blank=True, unique=True, null=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(
        choices=[("M", "Male"), ("F", "Female"), ("NA", "Other")],
        null=True,
        blank=True,
        max_length=2,
    )
    theme = models.CharField(
        choices=[("D", "Dark"), ("L", "Light")],
        default="D",
        null=True,
        blank=True,
        max_length=1,
    )
    profile_picture = models.ImageField(
        upload_to=image_path,
        max_length=100,
        default="build/profile_pictures/default_pfp.jpg",
    )
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
