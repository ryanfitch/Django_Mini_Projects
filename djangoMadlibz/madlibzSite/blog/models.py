from django.db import models


class Post(models.Model):
    date = models.DateTimeField()
    name = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    comment = models.CharField(max_length=140)
    body = models.TextField()


    def __str__(self):
        return self.title