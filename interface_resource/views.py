from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Interface
from .models import Reservation
from django.template import loader
from django.http import HttpResponse
import openpyxl
def home(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


def interface_resource(request):
    template = loader.get_template('orange2.html')
    search_ip = request.GET.get('ip', '')
    search_desc = request.GET.get('desc', '')
    search_rou = request.GET.get('rou', '')
    search_ad = request.GET.get('ad', '')
    per_page = int(request.GET.get('per_page', 10))

    # Always order by something to avoid pagination warning
    data = Interface.objects.all().order_by('id')

    # Apply filters
    if search_ip:
        data = data.filter(ipv4_address__icontains=search_ip)
    if search_desc:
        data = data.filter(description__icontains=search_desc)
    if search_rou:
        data = data.filter(ne_name__icontains=search_rou)
    if search_ad:
        data = data.filter(admin_status__icontains=search_ad)
    # Paginate
    paginator = Paginator(data, per_page)
    page = request.GET.get('page')

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)
    context = {
        'page_obj': page_obj,
        'per_page': per_page,
        'per_page_sizes': [20, 50, 100],
        'total_count': paginator.count,
        'search_ip': search_ip,
        'search_desc': search_desc,
        'search_rou': search_rou,
        'search_ad': search_ad,
        }
    

    return HttpResponse(template.render(context, request))
def reservation_porte(request):
    if request.method == 'POST':
        interface_name1 = request.POST['Inter']
        description1 = request.POST['Des']
        ne_name1 = request.POST['NE']

        reserva = Reservation(interface_name1=interface_name1, description1=description1, ne_name1=ne_name1)
        reserva.save()
    template = loader.get_template('reservation_porte.html')
    data1 = Reservation.objects.all().order_by('id')
    return render(request, 'reservation_porte.html', {'data1': data1})

