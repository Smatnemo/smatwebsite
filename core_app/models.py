from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Authors(models.Model):
    name = models.CharField(max_length=250)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Books(models.Model):
    author = models.ManyToManyField(Authors)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    cover = models.ImageField(upload_to='pics/covers/', default='pics/default-cover.jpg')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title