from django.db import models


class Novel(models.Model):
    class Meta:
        db_table = "novel"

    title = models.CharField(max_length=128)
    author_name = models.CharField(max_length=64)
    content = models.TextField()
    search_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
