from django.db import models

# Create your models here.

class DB_tucao(models.Model):
    user = models.CharField(max_length=30,null=True) #吐槽人姓名
    text = models.CharField(max_length=1000,null=True) #吐槽的内容
    ctime = models.DateTimeField(auto_now=True) #提交的时间
    def __str__(self):
        return self.text + str(self.ctime)


class DB_home_href(models.Model):
    name = models.CharField(max_length=30,null=True) #超链接的名字
    href = models.CharField(max_length=2000,null=True) #超链接的地址
    def __str__(self):
        return self.name