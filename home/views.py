from django.shortcuts import render


def home(request):
    """View function for home page of site."""

    # Render the HTML template home.html
    return render(request, 'home.html')
