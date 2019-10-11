"""oauth3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

# from allauth.socialaccount.models import SocialToken
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone


@login_required
def detail(request):
    # token = SocialToken \
    #     .objects \
    #     .filter(account__user=request.user, expires_at__gt=timezone.now(), app=1) \
    #     .first()
    token = None

    return JsonResponse({
        'user': {
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
        },
        'token': {
            'token': token.token,
            'expires_at': token.expires_at,
        } if token else None

        # 'auth': request.auth,registratiAn error occurred while attempting to login via your social network account.on/login.html
    })


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', detail),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^o/', include('oauth2_provider_jwt.urls', namespace='oauth2_provider_jwt')),
]
