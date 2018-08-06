from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
# Create your views here.
import os

def index(request):
    return HttpResponse('Index-page')




def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        # u = request.POST.get('user')
        # p = request.POST.get('pwd')
        # if u == 'admin' and p == '123':
        #     # 注意 redirect(跳转路径的'/')
        #     return redirect('/index/')
        # else:
        #     return render(request, 'login.html')
        # radio
        r = request.POST.get('gender')
        print(r)
        # checkbox
        f = request.POST.getlist('favor')
        print(f)

        # select
        s = request.POST.getlist('city')
        print(s)
        # upload
        file_obj = request.FILES.get('upload')
        print(file_obj.name)
        file_path = os.path.join('upload', file_obj.name)
        print(file_path)
        f = open(file_path, mode='wb')
        for item in file_obj.chunks():
            f.write(item)
        f.close()
        return render(request, 'login.html')
    else:
        return redirect('/index/')


from django.views import View


class Home(View):
    # 内部调用的dispach,dispatch的作用,接收请求，反射get,post,put,option等方法，然后拿到结果，将结果返回给用户
    # def dispatch(self, request, *args, **kwargs):
    #         print('before')
    #         result = super(Home, self).dispatch(request, *args, **kwargs)
    #         print('after')
    #         return result

    def get(self, request):
        print(request.method)
        return render(request, 'home.html')

    def post(self, request):
        print(request.method)
        return render(request, 'home.html')