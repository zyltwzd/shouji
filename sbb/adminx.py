
import xadmin
from daterange_filter.filter import DateRangeFilter
from sbb import models
from xadmin import views
from import_export import resources

#更改标题
class GlobalSetting(object):
    site_title = '设备管理'
    site_footer = '测试版本'
    menu_style = "accordion"

#更改图标
class sbbAdmin(object):
    model_icon = 'fa fa-home'
    list_display = ("sbb_type", "bianhao", "sn", "business_unit", "status")
#页面显示那些内容
    #搜索框
    #search_fields = ("sbb_type", "bianhao", "sn")
    list_filter = ("sbb_type", "business_unit", "status",)
    #及时编辑技术
    list_editable = ['status']
    #详细显示
    #show_detail_fields = ['createTime']
    #自动刷新
    #refresh_times = (3, 5)
    #导出格式设置 有问题
    #list_export = ('xls')
    #data_charts = {
    #    "user_count": {'title': u"图例", "x-field": "createTime", "y-field": ("age")}
    #    }

class SbbGzAdmin(object):
    model_icon = 'fa fa-home'
    list_display = ("sbb_type", "bianhao", "business_unit", "guzhang_time", "chuli_time", "zhibanyuan", "chuliren", "yanshouren")
#页面显示那些内容
    #搜索框
    #search_fields = ("sbb_type", "bianhao", "sn")
    list_filter = ("sbb_type", "business_unit", "chuli_time")
    #及时编辑技术
    list_editable = ['status']
    #详细显示
    #show_detail_fields = ['createTime']
    #自动刷新
    #refresh_times = (3, 5)
    #导出格式设置 有问题
    #list_export = ('xls')
    ##    "user_count": {'title': u"图例", "x-field": "chuliren", "y-field": (models.sbb_gz.objects.filter(sbb_type=0).count())}
#        }
class ShudiAdmin(object):
    model_icon = 'fa fa-home'
    list_display = ("name", "pname", "pnober")
#页面显示那些内容
    #搜索框
    #search_fields = ("name", "pname", "pnober")
    #及时编辑技术
    #list_editable = ['status']
    #详细显示
    #show_detail_fields = ['createTime']
    #自动刷新
    #refresh_times = (3, 5)
    #导出格式设置 有问题
    #list_export = ('xls')
    #data_charts = {
    #    "user_count": {'title': u"图例", "x-field": "createTime", "y-field": ("age")}
    #    }
class ManufacturerAdmin(object):
    model_icon = 'fa fa-home'
    list_display = ("name", "telephone", "memo")
#页面显示那些内容
    #搜索框
    #search_fields = ("name", "telephone", "memo")
    #及时编辑技术
    #list_editable = ['status']
    #详细显示
    #show_detail_fields = ['createTime']
    #自动刷新
    #refresh_times = (3, 5)
    #导出格式设置 有问题
    #list_export = ('xls')
    #data_charts = {
    #    "user_count": {'title': u"图例", "x-field": "createTime", "y-field": ("age")}
    #    }
#主题开启
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class ImgAdmin(object):
    model_icon = 'fa fa-home'
    list_display = ("img_url")



xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(models.sbb, sbbAdmin)
xadmin.site.register(models.sbb_gz, SbbGzAdmin)
xadmin.site.register(models.Img, ImgAdmin)
xadmin.site.register(models.Manufacturer, ManufacturerAdmin)
xadmin.site.register(models.Shudi, ShudiAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)