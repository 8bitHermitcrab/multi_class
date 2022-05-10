from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

# Controller
def index(request):
    # index 컨트롤러 생성
    # return HttpResponse("Hello, world. You're at the polls index.")
    # return render(request, 'index.html', {'name':'윤수'})

    user_list = ['윤수', '수지', '재현']

    role = 'superuser'

    # return render(request, 'index2.html', {'name':'윤수', 'user_list':user_list, 'role':role})
    # return render(request, 'base.html', {'name':'윤수', 'user_list':user_list, 'role':role})
    return render(request, 'index.html', {'name':'윤수', 'user_list':user_list, 'role':role})