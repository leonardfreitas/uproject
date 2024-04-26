from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView

from projects.models import Project

login_view = LoginView.as_view(template_name='login.html')
logout_view = LogoutView.as_view(next_page='core:login')


def home_view(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, 'home.html', context)