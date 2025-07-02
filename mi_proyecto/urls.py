"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from mi_proyecto import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola/', views.saludo),
    path('informacion/', views.informacion),
    path('mi_informacion/', views.mi_informacion),
    path('mi_nacionalidad/', views.mi_nacionalidad),
    path('edad/', views.edad),
    path('mi_hobby/', views.mi_hobby),
    path('mi_telefono/', views.mi_telefono),
    path('mi_email/', views.mi_email),
    path('mi_redes_sociales/', views.mi_redes_sociales),
    path('mi_curso/', views.mi_curso),
    path('mi_blog/', views.mi_blog),
    path('mi_github/', views.mi_github),
    path('calcular_edad/<int:anio>', views.calcular_edad),
    path('calcular_edad_pasada/<int:anio>', views.calcular_edad_pasada),
    path('suma_numeros/<int:n1>/<int:n2>/', views.suma_numeros),
    path('division/<int:numero1>/<int:numero2>/', views.division_exacta),
    path('pagina_html/', views.pagina_html),
    path('video_example/', views.video_example),
    path('header/', views.header),
    path('main/', views.main),
    path('section/', views.section),
    path('formulario/', views.formulario),
    path('registro/', views.registro),
    path('iconos/', views.iconos_saludo),
    path('login/', views.login),
    path('coro/', views.coro_blessd),
    path('cancion_piponas/', views.cancion_blessd_piponas),
    path('loader_example/', views.loader_example),
    path('render_example/', views.render_example),
    path('render_to_response_example/', views.render_to_response_example),
]

