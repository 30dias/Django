from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

User = get_user_model()

# Create your views here.
@login_required(login_url="/authentication/login/")
def rooms_view(request):
    unique_ips = User.objects.exclude(ip_address__isnull=True).values_list('ip_address', flat=True).distinct()
    
    ip_usernames = {}
    for ip in unique_ips:
        users_with_ip = User.objects.filter(ip_address=ip).values_list('username', flat=True)
        ip_usernames[ip] = list(users_with_ip)
    return render(request, 'rooms.html', {'ips': ip_usernames})