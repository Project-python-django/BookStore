from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# 主页



def home(request):
    pass

# -------------------业务-------------------
# todo 登录
def login(request):
    pass

# todo 登出
def logout(request):
    pass


def home(request):
    return JsonResponse({"msg": "ok"})