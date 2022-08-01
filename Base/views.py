from django.shortcuts import render
from Base.services.base_service import get_about, get_information

# Create your views here.

from django.contrib.auth.decorators import login_required

# @login_required(login_url='login/')
def view_about(request):
    information = get_information(request.user)
    information['founders'] = get_about()
    return render(
        request = request,
        template_name ='Base/footer.html',
        context = information
    )