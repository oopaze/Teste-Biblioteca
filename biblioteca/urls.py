"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from livro import urls as url_livro
from autor import urls as url_autor
from livro.views import exibir_livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', exibir_livros, name='home'),
    path('livros/', include(url_livro)),
    path('autores/', include(url_autor))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
