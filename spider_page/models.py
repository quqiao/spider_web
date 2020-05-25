from django.db import models

"""后台管理系统数据创建"""
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

# 新增一张用户表，表名为user 字段user_name, psw ,mail 都是字符串类型
class User(models.Model):
    user_name = models.CharField(max_length=100, primary_key=True)   # 设置为主键
    psw = models.CharField(max_length=100)
    mail = models.CharField(max_length=100)

"""爬虫各页面数据创建"""
class hezongyypy(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'hezongyy_py'

class longyitjzq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'longyi_tjzq'

class longyiyp(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)
    class Meta:
        managed = True
        db_table = 'longyi_yp'

class rjyiyaoxpsj(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'rjyiyao_xpsj'

class rjyiyaozkzq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'rjyiyao_zkzq'

class scjrmzszq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'scjrm_zszq'

class scjuchuangjtj(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'scjuchuang_jtj'

class scjuchuangpy(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'scjuchuang_py'

class scjuchuangtjzq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'scjuchuang_tjzq'

class scjuchuangyxzq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'scjuchuang_yxzq'

class sckxyyypzq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'sckxyy_ypzq'

class scytyytjzq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'scytyy_tjzq'

class scytyyzszq(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'scytyy_zszq'

class ysbangzxxd(models.Model):
    ID = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    cj = models.CharField(max_length=100)
    gg = models.CharField(max_length=100)
    xq = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    price2 = models.CharField(max_length=100)
    price3 = models.CharField(max_length=100)

    class Meta:
        managed = True
        db_table = 'ysbang_zxxd'