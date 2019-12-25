from django.db import models
from db.base_model import BaseModel
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser, BaseModel):
    """用户模型类"""

    # 元选项
    class Meta:
        # 定义数据表的名字
        db_table = 'df_user'

        # 命名后台用户数据标题名字
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class Address(BaseModel):
    """地址模型类"""
    receiver = models.CharField(max_length= 20, verbose_name= '收件人')
    addr = models.CharField(max_length= 256, verbose_name= '收件地址')
    zip_code = models.CharField(max_length= 6, null= True, verbose_name='邮件编码')
    phone = models.CharField(max_length= 11, verbose_name='联系电话')
    is_default = models.BooleanField(default=False, verbose_name= '是否为默认地址')
    # 一对多
    user = models.ForeignKey('User', verbose_name= '所属账户')

    # 元选项
    class Meta:
        # 定义数据表的名字
        db_table = 'df_address'

        # 命名后台用户数据标题名字
        verbose_name = '地址'
        verbose_name_plural = verbose_name

