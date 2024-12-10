from django.db import models

# Create your models here.
class Contact(models.Model):
    """
    Model to create contact form submission
    """
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email
