from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):   # 걍 request 해라. request로 받아서 하는게 편함.
                      # 요청에 의해 처리되는 함수는 파라미터 하나를 걸어서.요청에 의해 받는 값을 처리할수 있도록 하자.
    # return HttpResponse("my_to_do_app.urls")
    # 요청에 대한 응답객체를 생성해서 바로 클라이언트에 반환

    return render(request,'my_to_do_app/index.html')
#Templates/my_to_do_app/index.html 와 같은 뜻이긴 한데 이대로 쓰면 오류난다..




def createTodo(request):

    # 사용자가 메모에 입력해서 넘긴 값을 반환하는 코드

    # return HttpResponse("createTodo  메모 작성 합니다.~!!") # 요청에 응답하는지만 확인

