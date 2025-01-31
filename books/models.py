from django.db import models
import uuid

class Book(models.Model):
    STATUS_CHOICES = [
        ("available", "Available"),
        ("checked_out", "Checked Out"),
        ("lost", "Lost"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    publication_date = models.DateField()
    availability = models.CharField(max_length=20, choices=STATUS_CHOICES, default="available")
    edition = models.CharField(max_length=50, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

