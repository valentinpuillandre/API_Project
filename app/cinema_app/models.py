from django.db import models


class Viewer(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)

    class Meta:
        db_table = "users"
        managed = False

    def __str__(self):
        return self.name
