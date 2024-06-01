from django.db import models


class Category(models.Model):
    priority = models.IntegerField(default=0)
    identify = models.CharField(max_length=255)
    screen_name = models.CharField(max_length=255)

    def __str__(self):
        return self.screen_name
