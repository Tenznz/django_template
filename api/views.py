from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .forms import UserForm


def index(request):
    try:
        form = UserForm()
        if request.method == 'POST':
            print(request.POST)
            form = UserForm(request.POST)
            if form.is_valid():
                form.save()
        context = {'form': form}
        return render(request, 'index.html', context)
    except Exception as e:
        return HttpResponse(request, str(e))


# class StudentForm(APIView):
#     def get(self, request):
#         try:
#             form = UserForm()
#             context = {'form': form}
#             return render(request, 'index.html', context)
#         except Exception as e:
#             return HttpResponse(request, str(e))
