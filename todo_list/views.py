from django.views.generic import ListView,CreateView,UpdateView,FormView,DeleteView
from django.urls import reverse_lazy
from django.shortcuts import redirect
import uuid
from todo_list.models import *


from .models import Task

from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.
class CustomLoginView(LoginView):
    template_name='todo_list/login.html'
    fields='__all__'
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.get_user()
        # Check if the user has a wallet, if not, create one
        User_wallet.objects.get_or_create(user=user)
        return super().form_valid(form)
    
    def get_url_success(self):
        return reverse_lazy('home')
    
def CustomLogoutView(request):
     logout(request)
     return redirect(reverse_lazy('login'))

class RegisterPage(FormView):
    template_name='todo_list/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user = True
    success_url=reverse_lazy('home')

    def form_valid(self,form):
        user=form.save()
        User_wallet.objects.create(user=user)
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='tasks'

     # making changes to context
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        # context['tasks']= objects
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['count']=context['tasks'].filter(complete=False).count()

        # Fetch wallet information for the logged-in user
        try:
            user_wallet = User_wallet.objects.get(user=self.request.user)
            context['wallet_balance'] = user_wallet.balance
        except User_wallet.DoesNotExist:
            context['wallet_balance'] = 'No wallet found'

        #-----search bar------
        search_input=self.request.GET.get('q') or ''
        if search_input:
            context['tasks']=context['tasks'].filter(title__contains=search_input)
            # data in search bar
        context['search_input']=search_input

        return context

class CreateTask(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('home')

     # making changes to context
    def form_valid(self, form):
        # set authenticated user as user
        form.instance.user=self.request.user
        return super(CreateTask,self).form_valid(form)

class UpdateTask(LoginRequiredMixin,UpdateView):
    model=Task
    fields=['title','description','complete']
    success_url=reverse_lazy('home')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model=Task
    context_object_name='tasks'
    template_name='todo_list/task_delete.html'
    success_url=reverse_lazy('home')
    

