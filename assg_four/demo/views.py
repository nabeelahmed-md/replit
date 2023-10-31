from django.shortcuts import render
from .models import Region, Ticket
from datetime import datetime

def Home(request):
    if request.method == 'POST':
        time_str = request.POST['time']
        time = datetime.strptime(time_str, '%Y-%m-%dT%H:%M')
        region_id = request.POST['region']
        region = Region.objects.get(pk=region_id)
        day_of_week = time.strftime("%A")
        street_address = request.POST['street']
        ticket = Ticket(time=time, street_address=street_address, region=region, day=day_of_week)
        ticket.save()

    regions = Region.objects.all()
    return render(request, 'home.html', {'regions': regions})

def History(request):
    tickets = Ticket.objects.all()

    if request.method == 'POST':
        region_id = request.POST.get('region')
        day = request.POST.get('day')

        if region_id:
            tickets = tickets.filter(region=region_id)
        if day:
            tickets = tickets.filter(day=day)

    regions = Region.objects.all()
    return render(request, 'history.html', {'tickets': tickets, 'regions': regions})
