import os
from django.contrib.auth import get_user_model
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    User = get_user_model()
    if (
        os.getenv("CREATE_SUPERUSER") == "1"
        and not User.objects.filter(username=os.getenv("DJANGO_SUPERUSER_USERNAME")).exists()
    ):
        User.objects.create_superuser(
            username=os.getenv("DJANGO_SUPERUSER_USERNAME"),
            email=os.getenv("DJANGO_SUPERUSER_EMAIL"),
            password=os.getenv("DJANGO_SUPERUSER_PASSWORD"),
        )