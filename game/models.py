from django.db import models
#from main.models import Main_User

# # Create your models here.
# class User_Score(models.Model):
#     nickname = models.ForeignKey(Main_User,on_delete=models.CASCADE, db_column='nickname')
#     Score = models.IntegerField()

#     class Meta:
#         db_table = 'User_Score'
#         managed = True
        
class MyModel(models.Model):
    img = models.ImageField(upload_to='images/', default=0)
    name = models.TextField(max_length=20,default=0)

    class Meta:
        db_table = 'MyModel'
        managed = False


