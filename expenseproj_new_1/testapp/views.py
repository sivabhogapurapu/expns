from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from testapp.models import Expenses
from testapp.forms import ExpForm,SignupForm, User
from django.http import HttpResponseRedirect
from django.db.models import Sum, Count
from django.db.models.functions import Lower

# Create your views here.

def WelcomePageView(request):
    return render(request, 'testapp\default.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def ListPageView(request):
    username = request.user.username  # it gives me the user name logged in with.
    explist = Expenses.objects.all().filter(paidby__iexact=username)  # __iexact gives me the name with both upper and lower case
    person_total = Expenses.objects.filter(paidby__iexact=username).aggregate(Sum('amount'))['amount__sum']
    return render(request, 'testapp/listview.html', {'explist':explist, 'person_total':person_total})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def ListallPageView(request):
    explist = Expenses.objects.all()
    total = Expenses.objects.aggregate(Sum('amount'))['amount__sum']
    # dist_name=Expenses.objects.filter(paidby__iexact=request.user.username).aggregate(Count('paidby'))['paidby__count']
    # dist_name = Expenses.objects.values(lower('paidby')).distinct()
    dist_name=Expenses.objects.annotate(
                paidby_lower=Lower('paidby')).values_list('paidby_lower', flat=True).\
                order_by('paidby_lower').distinct().count() # get distinct records irrespective of case sensitive
    if (total>0 and dist_name)>0:
        perhead = total/dist_name
    return render(request, 'testapp/listallview.html', {'explist': explist, 'total': total, 'perhead': perhead})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def CreateExpView(request):
    form=ExpForm
    if request.method=='POST':
        form=ExpForm(request.POST)
        if form.is_valid:
            form.save()
        return redirect('/list')
    return render(request, 'testapp/create.html',{'form':form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def UpdateExpView(request,id):
    explist=Expenses.objects.get(id=id)
    if request.method=='POST':
        form=ExpForm(request.POST, instance=explist)
        if form.is_valid:
            form.save()
        return redirect('/list')
    return render(request, 'testapp/update.html',{'explist':explist})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def DeleteExpView(request,id):
    explist=Expenses.objects.get(id=id)
    explist.delete()
    return redirect('/list')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def logout_view(request):
    request.session.flush()
    return render(request, 'testapp/logout.html')

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def CreateUserView(request):
    form=SignupForm()
    if request.method=='POST':
        form = SignupForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request, 'testapp/createuser.html', {'form':form})
