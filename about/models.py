from django.db import models

# Create your models here.

class About(models.Model):
    """
    Stores About me text
    """
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
        # return self.content