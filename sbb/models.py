from django.db import models
from django.utils.html import format_html
import xadmin


class Img(models.Model):
    img_url = models.ImageField(upload_to='img')




class sbb(models.Model):
    """    设备分类    """
    sbb_type_choice = (
        (0, '测酒仪'),
        (1, '模拟机'),
        (2, '验卡器'),
        (3, '读卡器'),
        (4, '自助出退勤'),
        (5, '其他')
    )

    sbb_status = (
        (0, '在用'),
        (1, '备用'),
        (2, '返厂'),
        (3, '故障'),
        )

    sbb_type = models.SmallIntegerField(choices=sbb_type_choice, default=0, verbose_name="设备类型")
    bianhao = models.CharField(max_length=64, verbose_name="设备编号")     # 可重复
    sn = models.CharField(max_length=128, unique=True, verbose_name="固资编码")  # 不可重复
    business_unit = models.ForeignKey('Shudi', on_delete=models.CASCADE, verbose_name='属地')
    status = models.SmallIntegerField(choices=sbb_status, default=0, verbose_name='设备状态')
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE, null=True, blank=True, verbose_name='设备制造商')
    manage_ip = models.CharField(max_length=64, null=True, blank=True, verbose_name='远控ID')
    purchase_day = models.DateField(null=True, blank=True, verbose_name="生产日期")
    expire_day = models.DateField(null=True, blank=True, verbose_name="年检日期")
    chunqiu_day = models.DateField(null=True, blank=True, verbose_name="春鉴/秋整日期")
    price = models.FloatField(null=True, blank=True, verbose_name="价格")
    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')

    #def __str__(self):
    #    return '<%s>  %s' % (self.get_sbb_type_display(), self.name)

    #def status(self):
    #   if self.status == "故障":
    #        color_code = 'red'
    #    else:
    #        color_code = 'green'
    #    return format_html(
    #               '<span style="color:{};">{}</span>',
    #                color_code,
    #                self.status,
     #   )
    class Meta:
        verbose_name = '设备总表'
        verbose_name_plural = "设备总表"
        ordering = ['-m_time']


class sbb_gz(models.Model):
    """    设备分类    """
    sbb_gz_type_choice = (
        (0, '测酒仪'),
        (1, '模拟机'),
        (2, '验卡器'),
        (3, '读卡器'),
        (4, '自助出退勤'),
        (5, '其他')
    )

    sbb_type = models.SmallIntegerField(choices=sbb_gz_type_choice, default=0, verbose_name="设备类型")
    bianhao = models.CharField(max_length=64, verbose_name="设备编号")     # 可重复
    business_unit = models.ForeignKey('Shudi', on_delete=models.CASCADE, verbose_name='属地')
    guzhang_time = models.DateTimeField(null=True, blank=True, verbose_name="故障时间")
    chuli_time = models.DateTimeField(null=True, blank=True, verbose_name="处理时间")
    zhibanyuan = models.CharField(max_length=16, verbose_name="值班员")
    chuliren = models.CharField(max_length=16, verbose_name="处理人")
    yanshouren = models.CharField(max_length=16, verbose_name="验收人")
    memo = models.TextField(null=True, blank=True, verbose_name='备注')
    m_time = models.DateTimeField(auto_now=True, verbose_name='更新日期')


    #def __str__(self):
     #   return '<%s>  %s' % (self.get_sbb_type_display(), self.name)

    #def status(self):
    #   if self.status == "故障":
    #        color_code = 'red'
    #    else:
    #        color_code = 'green'
    #    return format_html(
    #               '<span style="color:{};">{}</span>',
    #                color_code,
    #                self.status,
     #   )
    class Meta:
        verbose_name = '设备故障记录表'
        verbose_name_plural = "设备故障记录表"
        ordering = ['-m_time']


class Manufacturer(models.Model):
    """厂商"""

    name = models.CharField('厂商名称', max_length=64, unique=True)
    telephone = models.CharField('支持电话', max_length=30, blank=True, null=True)
    memo = models.CharField('备注', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '厂商'
        verbose_name_plural = "厂商"


class Shudi(models.Model):
    """属地"""

    name = models.CharField('属地', max_length=64, unique=True)
    pname = models.CharField('联系人', max_length=64, blank=True, null=True)
    pnober = models.CharField('电话', max_length=64, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '属地'
        verbose_name_plural = "属地"

