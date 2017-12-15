from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    from hfapp.models.color import Color
    
    lines = [
        "Red       == red?       %s" % (Color.objects.get(pk="red") == Color.RED),
        "Green     == green?     %s" % (Color.objects.get(pk="green") == Color.GREEN),
        "Blue      == blue?      %s" % (Color.objects.get(pk="blue") == Color.BLUE),
        "Colorless == colorless? %s" % (Color.objects.get(pk="colorless") == Color.COLORLESS)
    ]
    
    return HttpResponse('\n'.join(lines))