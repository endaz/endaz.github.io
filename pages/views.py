from django.shortcuts import render

# Create your views here.

nav_menu = [
    {
        "name": "Kosa",
        "url": "/kosa/",
        "validators": [],
        "submenu": [
            {
                "name": "Farbanje kose",
                "url": "/kosa/farbanje-kose/",
                "validators": [],
                "submenu": []
            }
        ]
    },
    {
        "name": "Nokti",
        "url": "/nokti/",
        "validators": [],
        "submenu": [
            {
                "name": "Manikir",
                "url": "/nokti/manikir/",
                "validators": [],
                "submenu": [
                    {
                        "name": "Vatra i led SPA manikir",
                        "url": "/nokti/manikir/vatra-i-led-spa-manikir/",
                        "validators": [],
                        "submenu": []
                    },
                ]
            },
            {
                "name": "Pedikir",
                "url": "/nokti/pedikir/",
                "validators": [],
                "submenu": []
            },
            {
                "name": "Nadogradnja",
                "url": "/nokti/nadogradnja/",
                "validators": [],
                "submenu": []
            }
        ]
    },
    {
        "name": "Oči, obrve & trepavice",
        "url": "/oci-obrve-trepavice/",
        "validators": [],
        "submenu": [
            {
                "name": "Farbanje obrva",
                "url": "/oci-obrve-trepavice/farbanje-obrva/",
                "validators": [],
                "submenu": []
            }
        ]
    },
    {
        "name": "Masaže",
        "url": "/masaze/",
        "validators": [],
        "submenu": [
            {
                "name": "Švedska relax",
                "url": "/masaze/svedska-relax/",
                "validators": [],
                "submenu": []
            }
        ]
    },
    {
        "name": "Depilacija",
        "url": "/depilacija/",
        "validators": [],
        "submenu": [
            {
                "name": "Depilacija brade",
                "url": "/depilacija/depilacija-brade/",
                "validators": [],
                "submenu": []
            }
        ]
    },
    {
        "name": "Tretmani lica",
        "url": "/tretmani-lica/",
        "validators": [],
        "submenu": [
            {
                "name": "Higijensko cišcenje lica",
                "url": "/tretmani-lica/higijensko-cišcenje-lica/",
                "validators": [],
                "submenu": []
            }
        ]
    }
]


def home(request):
    context = {
        "nav_menu": nav_menu
    }
    return render(request, 'pages/home.html', context)


def profession_category(request):
    context = {
        "nav_menu": nav_menu
    }
    return render(request, 'pages/profession_category.html', context)


def profession(request):
    context = {
        "nav_menu": nav_menu
    }
    return render(request, 'pages/profession.html', context)


def profile(request):
    context = {
        "nav_menu": nav_menu
    }
    return render(request, 'pages/profile.html', context)


def register(request):
    context = {
        "nav_menu": nav_menu
    }
    return render(request, 'pages/register.html', context)

