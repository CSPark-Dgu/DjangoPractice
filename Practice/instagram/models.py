from django.db import models
from django.conf import settings


class Post(models.Model):
    message = models.TextField()
    photo = models.ImageField(blank=True, upload_to="instagram/%Y/%m/%d")
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Custom Post object ({self.id})"

    def message_length(self):
        return len(self.message)

    class Meta:
        ordering = ["-id"]
