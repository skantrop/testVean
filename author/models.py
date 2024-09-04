from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateTimeField(blank=True, null=True)


    def __str__(self) -> str:
        return self.name
