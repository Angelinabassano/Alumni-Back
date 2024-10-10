from django.http import JsonResponse
from .models import School

def school_list(request):
    schools = School.objects.values_list('name', flat=True)
    return JsonResponse(list(schools), safe=False)

