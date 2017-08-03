from django.db import models

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100);
    limit = models.IntegerField();
    status = models.BooleanField();
    address = models.CharField(max_length=200);
    start_time = models.DateTimeField('events time');
    create_time = models.DateTimeField(auto_now=True);

    def __str__(self):
        return self.name;

# 嘉宾表
class Guest(models.Model):
    event = models.ForeignKey(Event) # 关联发布会 id
    realname = models.CharField(max_length=64) # 姓名
    phone = models.CharField(max_length=16) # 手机号
    email = models.EmailField() # 邮箱
    sign = models.BooleanField() # 签到状态
    create_time = models.DateTimeField(auto_now=True) # 创建时间（自动获取当前时间）
    class Meta:
        unique_together = ("event", "phone")
    def __str__(self):
        return self.realname

#测试用的表
class Test(models.Model):
    name = models.CharField(max_length=20);
    age = models.IntegerField();