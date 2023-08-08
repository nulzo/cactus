from django.shortcuts import render


# Create your views here.
def home(request):
    text = {
        "Track Your Spending": "Track that thang yup!",
        "Stay on Budget": "I am some samlpe text",
    }
    context = {"text": text}
    return render(request, template_name="home/home.html", context=context)
