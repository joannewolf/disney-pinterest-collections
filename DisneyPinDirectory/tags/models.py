from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'name': self.name,
        }


class Tag(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    color = models.CharField(max_length=20, null=False, blank=False)

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category.as_dict(),
            'color': self.color,
        }

    def as_simple_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
        }
