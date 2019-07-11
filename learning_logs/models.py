from django.db import models

class Topic(models.Model):
    # A topic that the user is learning about.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return a string representation of the model.
        return self.text

class Entry(models.Model):
    # Some details about the topic you've created.
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        # Return the first 50 characters followed by "..."
        return self.text[:50] + "..."

