#Create data model

# models.py 
from django.db import models

class Customer(models.Model):

    # database, display
    TYPE_CHOICES = (
        ('Customer', 'Customer'),
        ('Supplier', 'Supplier'),
        ('Student', 'Student'),
    )

    name = models.Charfield('Article name', max_length=120)
    note = models.TextField(blank=True, null = True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    credit = models.FloatField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type = models.CharField(choices=TYPE_CHOICES)

    def __str__(self): 
        return self.name

# User for Auth and more
# Add to settings.py: AUTH_USER_MODEL = 'app_name.User'
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    # Inherits AbstractUser fields
    pass

# One-to-Many: (use double quotes if the entity is not yet declare) ex. "Supplier"
supplier = models.ForeignKey(Supplier, blank=True, null=True, on_delete=models.CASCADE)

# Many-to-Many: 
tags = models.ManyToManyField(Tag, blank=True)

# One to One 
User = models.OneToOneField(User, on_delete=models.CASCADE)

# Overwrite save method
def save(self, (*args, **kwargs):
    if not self.slug:
        self.slug = slugify(self.title)

    super().save(*args, **kwargs)