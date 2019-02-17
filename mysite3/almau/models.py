from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)
    groups = models.ManyToManyField('Group')
    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
