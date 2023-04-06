from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    color = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name
