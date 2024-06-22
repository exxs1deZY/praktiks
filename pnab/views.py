from django.shortcuts import render, redirect
from .models import User, Stament
from django.contrib.auth.hashers import check_password
from django.contrib.auth import logout


def reg(request):
    error = ''
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        role = 'Пользователь'
        if not User.objects.filter(email=email).exists():
            user = User(name=name, email=email, password=password, role=role)
            user.save()
            request.session['user_id']=user.id
            return redirect(home)
        else:
            error = 'Такой польззователь уже есть!'
    return render(request, 'reg.html', {'error':error})

def auth(request):
    error = ''
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user_id']=user.id
                return redirect(home)
            else:
                error = 'Ошибка в пароле!'
        except User.DoesNotExist:
            error = 'Ошибка в почте!'
    return render(request, 'auth.html', {'error':error})


def home(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        statements = Stament.objects.filter(user=user)
        return render(request, 'home.html', {'statements':statements})
    else:
        return redirect(auth)


def add_statement(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        if request.method == 'POST':
            name = request.POST['name']
            text = request.POST['text']
            number_car = request.POST['number_car']
            user = user
            otvet = 'Новый'
            image = request.FILES.get('image')
            statement = Stament(name=name, text=text, number_car=number_car, user=user, otvet=otvet, image=image)
            statement.save()
            return redirect('home')
        return render(request, 'add_statement.html')
    else:
        return redirect('auth')


def logOut(request):
    logout(request)
    return redirect(auth)


def admin(request):
    if 'user_id' in request.session:
        user_id = request.session.get('user_id')
        user = User.objects.get(pk=user_id)
        if user.role =='Администратор':
            statements = Stament.objects.all()
            return render(request, 'admin.html', {'statements':statements})
        else:
            return redirect(auth)
    else:
        return redirect(auth)


def Otvet(request, statement_id):
    statement = Stament.objects.get(pk=statement_id)
    if request.method == 'POST':
        otvet = request.POST['otvet']
        statement.otvet=otvet
        statement.save()
        return redirect(admin)


def Delete(request, statement_id):
    statement = Stament.objects.get(pk=statement_id)
    if request.method=='POST':
        statement.delete()
        return redirect(admin)