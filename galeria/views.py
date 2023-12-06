from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#pg inicial
def home(request):
    return render(request, 'home.html')

#def index(request):
   # return render(request, 'index.html')

#Forms de cadastro usuário
def create(request):
    return render(request, 'create.html')

#Inserção de dados dos usuários no banco
def store(request):
    data = {}

    if 'password' in request.POST and 'password-conf' in request.POST:
        password = request.POST['password']
        password_conf = request.POST['password-conf']

        if password != password_conf:
            data['msg'] = 'Senha e confirmação de senha diferentes'
            data['class'] = 'alert-danger'
            return render(request, 'create.html', data)
        
    

    else:
        data['msg'] = 'Campos de senha ausentes no formulário'
        data['class'] = 'alert-danger'
        return render(request, 'create.html', data)

    

    # Restante do código para o caso em que a validação é bem-sucedida
    user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
    user.last_name = request.POST['lastName']
    user.first_name = request.POST['name']
    user.save()
    data['msg'] = 'Dados armazenados com sucesso'
    data['class'] = 'alert-success'
    return render(request, 'create.html', data)

#forms painel login
def painel(request):
    return render(request, 'painel.html')

#processa login
def dologin(request):
    data = {}
    user = request.POST["user"]
    password = request.POST["password"]
    user = authenticate(request, username=user, password=password)
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou senha inválidos'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)

#pagina inicial pós login    
@login_required
def dashboard(request):
    return render (request, 'dashboard/home.html')


#logout sistema
def logouts(request):
    logout(request)
    return redirect ('/painel/')


#acesso sem login - inválido
def notlogin(request):
    return render(request, 'notlogin.html')


#alterar senha
@login_required
def changePassword(request):
    data = {}
    senha_atual = request.POST['senha_atual']
    user = User.objects.get(email=request.user.email)
    user_authenticated = authenticate(request, username=request.user.username, password=senha_atual)

    if user_authenticated:
        nova_senha = request.POST["nova_senha"]
        confirmar_senha = request.POST['confirmar_senha']

        if nova_senha == confirmar_senha:
            user.set_password(nova_senha)
            user.save()
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('/painel/')
        else:
            data['msg'] = 'Confirmar senha diferente da nova senha!'
            data['class'] = 'alert-danger'
    else:
        data['msg'] = 'Senha atual incorreta'
        data['class'] = 'alert-danger'
    return render(request, 'dashboard/changePassword.html', data)
    


#caminho form alterar senha
def formChangePassword(request):
    return render(request, 'dashboard/changePassword.html')

