from django.http import HttpResponse, JsonResponse
from .rss import getEntry

def index(request):
    rssFeedURL = "https://qubit.hu/feed"
    return JsonResponse(
        {
            "entries": getEntry("https://qubit.hu/feed"),
            "URL": rssFeedURL,
        },
        json_dumps_params={'ensure_ascii': False},
    )
