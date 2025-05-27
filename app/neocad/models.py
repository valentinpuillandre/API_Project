from django.db import models


class Comment(models.Model):
    author = models.EmailField()
    comment = models.TextField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.author} - {self.timestamp}"


class NonConformity(models.Model):
    class Meta:
        db_table = "neocad"
        managed = False

    company_id = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    reported_by = models.EmailField()
    issue_type = models.CharField(max_length=50)
    description = models.TextField()
    photos = models.JSONField(blank=True, null=True)  # liste d'URLs photo
    severity = models.CharField(max_length=20)
    tags = models.JSONField(blank=True, null=True)  # liste de tags
    custom_fields = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=50)

    comments = models.ManyToManyField(Comment, blank=True)

    def __str__(self):
        return f"{self.company_id} - {self.issue_type} ({self.status})"
