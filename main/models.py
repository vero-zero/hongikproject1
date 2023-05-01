from django.db import models

class Main_User(models.Model):
    nickname = models.CharField(max_length=20)
    score = models.IntegerField(default=0)
    class Meta:
        db_table = 'Main_User' #연결할 테이블 명 
        managed = True #데이터
    