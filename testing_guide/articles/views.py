from django.shortcuts import render

# Create your views here.
def my_view(request):
    return render(request=request, template_name='articles/base.html')
