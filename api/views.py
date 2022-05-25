from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView

from .forms import UserForm


def index(request):
    return render(request, 'index.html')


class StudentForm(APIView):
    def get(self, request):
        try:
            # serializer = UserSerializer(data=request.data)
            # serializer.is_valid(raise_exception=True)
            # serializer.save()
            form = UserForm()
            context = {'form': form}
            return render(request, 'index.html', context)
        except Exception as e:
            return HttpResponse(request, str(e))
