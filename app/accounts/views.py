from django.shortcuts import render
from django.views import View
from django.urls import reverse
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from accounts.forms import CustomRegisterForm, UserLoginForm


class RegisterView(View):
    form = CustomRegisterForm
    template_name = "accounts/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form
        return render(request, self.template_name, context={"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"註冊成功，請登入您的帳號。" )
            return HttpResponseRedirect(reverse("accounts:login"))
        else:
            messages.error(request, '請檢查您的註冊資料。')
        return render(request, self.template_name, context={"form": form}) 



class CustomLoginView(View):
    form = UserLoginForm
    template_name = 'accounts/login.html'
    
    def get(self, request, *args, **kwargs):
        context = {'form': self.form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
                )
            if user is not None:
                login(request, user)
                messages.success(request, f"哈囉，<b>{user.username}</b>，登入成功。" )
                return HttpResponseRedirect(reverse('accounts:index'))
            else:
                messages.error(request, "帳號無效，請檢查您的帳號密碼。" )
        else:
            messages.error(request, '請檢查您的帳號、密碼。')
        return HttpResponseRedirect(reverse('accounts:login'))


@login_required
def custom_logout(request):
    logout(request)
    messages.success(request, "登出成功!")
    return HttpResponseRedirect(reverse("accounts:index"))


@login_required(login_url='accounts:login')
def index(request):
    return render(request, 'accounts/index.html')

