#:Signals

# models.py
from django.db.models.signals import post_save, pre_save

def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


# Launch the post_user_create_singal method if User model is save
post_save.connect(post_user_created_signal, sender=User)