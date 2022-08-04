from django.views.generic import View
fron django.shortcuts import render

class HomeView(View):
    def get(self, request, *args, **kwargs):
      context={
      
      }
      return render(request, '', context)
