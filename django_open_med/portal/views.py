from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
def login_sucess(request):
    if request.user.has_perm('users.custom_staff'):
        return redirect("/dashboard")
    else:
        return redirect("/portal")
