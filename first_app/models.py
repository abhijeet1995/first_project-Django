from django.db import models


class Topic(models.Model):
    top_name = models.CharField(max_length=240, unique=True)

    def __str__(self):
        return self.top_name


class WebPage(models.Model):
    topic = models.ForeignKey(Topic)
    name = models.CharField(max_length=264, unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name


class AccessRecord(models.Model):
    name = models.ForeignKey(WebPage)
    date = models.DateField()

    def __str__(self):
        return str(self.date)


class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    contact = models.BigIntegerField()

    def __str__(self):
        return self.name
