"""
Signal handlers for automatically creating and saving Profile instances
when User instances are created or updated.
"""

from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import Profile, User


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Create a Profile instance for each new User instance.
    """
    if created:
        Profile.objects.create(user=instance)
        instance.profile.save()


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Save the associated Profile instance when a User instance is updated.
    """
    instance.profile.save()
