from django.db import models

class MyModel(models.Model):
    img = models.ImageField(upload_to='images/', default=0)
    name = models.TextField(max_length=20,default=0)

    class Meta:
        db_table = 'MyModel'
        managed = False


