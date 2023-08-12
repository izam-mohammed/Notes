from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()
# Create your models here.


class Notes(models.Model):
    """
    Represents a user's note.

    Attributes:
    - user (ForeignKey): The user who owns the note.
    - created_at (DateTimeField): The timestamp of when the note was created.
    - title (CharField): The title of the note (limited to 100 characters).
    - caption (TextField): The content of the note.

    Methods:
    - __str__(): Returns a string representation of the note (title).
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
    title = models.CharField(max_length=100)
    caption = models.TextField()

    def __str__(self):
        """
        Returns a string representation of the note (title).

        Returns:
        - str: The title of the note.
        """
        return self.title
