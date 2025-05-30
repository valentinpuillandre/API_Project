from django.db import models


class NonConformity(models.Model):
    class Meta:
        db_table = "neocad"
        managed = False

    company_id = models.CharField(max_length=100)
    site_id = models.CharField(max_length=100)
    reported_by = models.EmailField()
    issue_type = models.CharField(max_length=50)
    description = models.TextField()
    photos = models.JSONField(blank=True, null=True)
    severity = models.CharField(max_length=20)
    tags = models.JSONField(blank=True, null=True)
    custom_fields = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=50)
    comments = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.company_id} - {self.issue_type} ({self.status})"
