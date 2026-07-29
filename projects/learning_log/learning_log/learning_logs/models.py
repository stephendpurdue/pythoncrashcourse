from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True) # Automatically fetches the time, set as a bool

    def __str__(self):
        """Return the model as a string"""
        return self.text

class Entry(models.Model):
    "Topic information"
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        if len(self.text) < 50:
             return self.text[:50] + "..."
        else:
            return self.text
       