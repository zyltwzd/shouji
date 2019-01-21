from django.shortcuts import render
from sbb import models

# Create your views here.
def uploadImg(request): # 图片上传函数
    if request.method == 'POST':
        img = models.Img(img_url=request.FILES.get('img'))
        img.save()
        imgs = models.Img.objects.all() # 从数据库中取出所有的图片路径
        context = {
        'imgs' : imgs
        }
    return render(request, 'imgupload.html', context)


def showImg(request):
    imgs = models.Img.objects.all() # 从数据库中取出所有的图片路径
    context = {
        'imgs' : imgs
    }
    return render(request, 'showImg.html', context)
