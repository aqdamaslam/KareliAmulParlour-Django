from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from kap.models import DairyProduct, Amul_1_Ltr_Ice_Cream_Tubs, Amul_2_Ltr_Ice_Cream_Bricks, Amul_750ml_Ice_Cream_Bricks
from django.shortcuts import render,get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    return render(request, 'index.html')

def dairy_products(request):
    lst = DairyProduct.objects.all()
    return render(request, 'dairy_products.html', {'lst':lst})


def ice_cream(request):
    ice1 = Amul_1_Ltr_Ice_Cream_Tubs.objects.all()
    lmn = Amul_2_Ltr_Ice_Cream_Bricks.objects.all()
    m3 = Amul_750ml_Ice_Cream_Bricks.objects.all()
    return render(request, 'ice_cream.html', {'ice1': ice1, 'lmn': lmn, 'm3': m3})
    return render(request, 'ice_cream.html')


def contact(request):

    name = request.POST.get('name')
    ice = str(request.POST.get('ice'))
    mob = str(request.POST.get('ph_1'))
    email = request.POST.get('email')
    query = str(request.POST.get('query'))

    subject = 'Kareli Amul Parlour : Your Query is/are: ' + ice
    message= 'Your Query : \n \n ' + query +  mob
    from_email = settings.EMAIL_HOST_USER
    to_list = [email, from_email]
    send_mail(subject, message, from_email, to_list, fail_silently= False)

    return render(request, 'contact.html')

def thanks(request):
    return render(request, 'thanks.html')


def delivery(request):
    return render(request, 'delivery.html')


def search_list(request):
    str = request.POST.get('query')
    if str:
        match_1 = DairyProduct.objects.filter(Q(name__icontains = str) | Q(desc__icontains = str))
        match_2 = Amul_2_Ltr_Ice_Cream_Bricks.objects.filter(Q(name__icontains = str) | Q(desc__icontains = str))
        match_3 = Amul_1_Ltr_Ice_Cream_Tubs.objects.filter(Q(name__icontains = str) | Q(desc__icontains = str))
        match_4 = Amul_750ml_Ice_Cream_Bricks.objects.filter(Q(name__icontains = str) | Q(desc__icontains = str))
        if match_1 or match_2 or match_3 or match_4:
            return render(request, 'search_list.html', {'m1': match_1, 'm2': match_2, 'm3': match_3, 'm4': match_4})
    if str:

        if match_2:
            return render(request, 'search_list.html', {})
        else:
            messages.error(request, 'No Result Found')
            print('Not Available')
    else:
        return HttpResponseRedirect('/search_list.html')
    return render(request, 'search_list.html')
