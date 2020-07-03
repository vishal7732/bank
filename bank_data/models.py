from django.db import models

class bankinfo(models.Model):
    name = models.CharField(max_length=100)
    ifsc = models.IntegerField(max_length=12, default = 0)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name
