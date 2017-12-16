from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    from hfapp.models.color import Color
    
    lines = [
        "Red       == red?       %s" % (Color.objects.get(pk='1R') == Color.RED),
        "Green     == green?     %s" % (Color.objects.get(pk='2G') == Color.GREEN),
        "Blue      == blue?      %s" % (Color.objects.get(pk='3B') == Color.BLUE),
        "Colorless == colorless? %s" % (Color.objects.get(pk='4_') == Color.COLORLESS)
    ]
    
    return HttpResponse('<br>'.join(lines))