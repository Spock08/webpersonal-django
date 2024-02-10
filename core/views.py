from django.shortcuts import render, HttpResponse

# Create your views here.

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li><a href="/">Portada</a></li>    
    <li><a href="/about/">About me</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contact</a></li>    
</ul>
"""

def home(request):
    return HttpResponse(
        html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
        """
    )


def about(request):
    return HttpResponse(
        html_base + """
        <h2>About Me</h2>
        <p>Mi Nombre es Emilio</p>
        """
    )

def portfolio(request):
    return HttpResponse(
        html_base + """
        <h2>Portfolio</h2>
        <p>Estos son mis trabajos</p>
        """
    )

def contact(request):
    return HttpResponse(
        html_base + """
        <h2>Contact</h2>
        <p>Escriba al mail: <a href="mailto:hola@hola.com">hola@hola.com</a></p>
        """
    )