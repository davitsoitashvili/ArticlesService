from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    photo_Url = models.CharField(max_length=300)
    body = models.TextField()
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


