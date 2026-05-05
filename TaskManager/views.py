from django.shortcuts import render, redirect
from tasks.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import  authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# view for adding tasks
@login_required(login_url='login')
def add_task(request):
    if request.method == 'POST':
        data = request.POST
        title = data.get('title')
        dic = data.get('dic')
        due_date = data.get('due_date')
        status = data.get('status')
        category_name = data.get('category')

        print(title, dic, due_date, status, category_name)

         # Fetch or create the Category instance
        category, created = Category.objects.get_or_create(name=category_name)

        Task.objects.create(
            title = title,
            dic = dic,
            due_date = due_date,
            status = status,
            category = category
        )
        # Redirect back to the same view to see the updated list
        return redirect('task')  # Ensure the redirect is working by using a named URL or full path

    # For GET requests, retrieve all tasks and render the template
    tasks = Task.objects.all()  # Fetch all tasks

    if request.GET.get('search'):
        tasks = tasks.filter(title__icontains = request.GET.get('search'))

    context = {'tasks': tasks}
    return render(request, 'tasks.html', context)

def delete(request, id):
    queryset = Task.objects.get(id = id)
    queryset.delete()
    return redirect('task')

def edit_task(request, id):
    task = Task.objects.get(id=id)
    
    if request.method == 'POST':
        title = request.POST.get('title')
        dic = request.POST.get('dic')
        due_date = request.POST.get('due_date')
        status = request.POST.get('status')
        category_name = request.POST.get('category')  # This is the string from the form
        

        # Retrieve or create the Category instance
        category, created = Category.objects.get_or_create(name=category_name)

        # Update the task fields
        task.title = title
        task.dic = dic
        task.due_date = due_date
        task.status = status
        task.category = category  # Assign the Category instance

        task.save()
        return redirect('task')

    return render(request, 'edit_task.html', {'task': task})

def login_task(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        # Check if the user exists
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid username")
            return redirect('login')
        
        # Authenticate user
        user = authenticate(username=username, password=password)

        if user is None:
            messages.info(request, "Invalid password")
            return redirect('login')
        else:
            login(request, user)
            return redirect('task')  # Redirect to task page on successful login

    return render(request, 'login.html')


def reg_task(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        u = User.objects.filter(username=username)

        if u.exists():
            messages.info(request, "User name already exist")
            return redirect('register')

        user = User.objects.create(
            username = username,
            )
        user.set_password(password)
        user.save()

        messages.info(request, "Account created")
        redirect('register')
        
    return render(request, 'reg.html')


def logout_page(request):
    logout(request)
    return redirect('login')
