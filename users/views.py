from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Регистрация нового пользователя."""
    if request.method != "POST":
        # Показывать форму регистрации.
        form = UserCreationForm()
    else:
        # Обработка заполненной формы.
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            login(request, new_user)
            return redirect('learning_logs:index')

    # Показать бланк или недействительную форму.
    context = {'form': form}
    return render(request, "registration/register.html", context)
