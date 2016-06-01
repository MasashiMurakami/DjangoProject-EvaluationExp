from django.db import models

# Create your models here.
class evaluation201606(models.Model):
    name = models.CharField(
        max_length=64,
        verbose_name='名前',
        help_text='お名前を入力してください',
        )
    
    rate = models.FloatField(
        verbose_name='正解率',
        blank=True,
        default=0.0,
        )
    
    time = models.FloatField(
        verbose_name='時間',
        blank=True,
        default=0.0,
        )
    
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='登録日時',
        )
    
