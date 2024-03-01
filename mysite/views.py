from django.http import HttpResponse

def home(request):
    return HttpResponse('''<h1>Welcome to voting APP</h1>
    <a href="http://127.0.0.1:8000/polls/" > Click here to begin  </a> '''                  
                        )