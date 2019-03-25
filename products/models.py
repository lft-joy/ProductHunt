from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Product(models.Model):
    title = models.CharField(default='例:app名称', max_length=50)
    intro = models.TextField(default='app介绍')
    icon = models.ImageField(default='default.png', upload_to='image/')

    votes = models.IntegerField(default=1)
    pub_date = models.DateTimeField()
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
