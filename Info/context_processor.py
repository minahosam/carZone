from .models import *

def get_main_info(request):
    owner_info = Info.objects.last()
    return {'footer': owner_info}