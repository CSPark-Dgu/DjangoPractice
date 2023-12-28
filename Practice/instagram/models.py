from django.db import models
from django.conf import settings

# from django.contrib.auth.models import User   #User 모델 변경 가능성 존재. 권장 하지 않음


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
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


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, limit_choices_to={"is_public": True}
    )  # post_id가 된다.
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
