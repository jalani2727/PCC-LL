from django.db import models

class Topics(models.Model):
    # A topic that the user is learning about.
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Return a string representation of the model.
        return self.text

