from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=140)
    body = models.TextField()
    name = models.CharField(max_length=140)
    comment = models.CharField(max_length=140)
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    # class Meta:
        # verbose_name = "Blog Entry"
        # verbose_name_plural = "Blog Entries"
        # ordering = ["-created"]