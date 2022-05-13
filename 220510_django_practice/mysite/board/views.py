from django.http import HttpResponse
from django.shortcuts import redirect, render
from.models import Board
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


def board_list(request):
    # Board조회
    board_list = Board.objects.all() # DB에서 모든 데이터 가져오는 함수.
    return render(request, 'board_list.html', {'board_list':board_list})

def board_write(request):
    print("요청 method", request.method)
    if request.method == "POST":
        data = request.POST
        Board.objects.create(
            title=data['title'],
            contents=data['content'])

        return redirect('/board')
    else:
        pass
    return render(request, 'board_write.html')

def board_detail(request, board_id):
    print(board_id)
    board = Board.objects.get(id=board_id)
    comments = board.comment_list.all()
    return render(request, 'board_detail.html', {'board':None})