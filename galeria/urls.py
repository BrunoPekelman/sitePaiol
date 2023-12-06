from django.urls import path
from galeria.views import create, store, painel, dologin, home, dashboard, logouts, notlogin, changePassword, formChangePassword

urlpatterns = [
    path('', home),
    #path('index/', index),
    path('create/', create),
    path('store/', store),
    path('painel/', painel),
    path('dologin/', dologin),
    path('dashboard/', dashboard),
    path('home/', home),
    path('logouts/', logouts),
    path('accounts/login/', notlogin),
    path('changePassword/', changePassword),
    path('formChangePassword/', formChangePassword)
]