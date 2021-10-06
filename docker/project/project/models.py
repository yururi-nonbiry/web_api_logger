import uuid
from django.db import models
from django.utils import timezone

# ログリスト
class log_list(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) # データの個体識別番号
    datetime = models.DateTimeField(null=True, default=timezone.now) # 保存した日時
    serial_no = models.CharField(null=True,max_length=30) # 測定器のシリアル
    voltage = models.FloatField(null=True) # 電池電圧
    temp = models.FloatField(null=True) # 気温
    humidity = models.FloatField(null=True) # 湿度
    atmospheric_pressure = models.FloatField(null=True) # 大気圧
    moisture_content = models.FloatField(null=True) # 含水量
    