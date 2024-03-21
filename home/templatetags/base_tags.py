from django import template
from django.forms import TextInput
from django.shortcuts import get_object_or_404

from portfolio.models import Portfolio
from menu.models import MenuCategory, Menu
from contact.forms import ContactForm


register = template.Library()


@register.inclusion_tag("home/partials/portfolio.html")
def portfolio():
    return {
        "portfolios": Portfolio.objects.published()
    }


@register.inclusion_tag('home/partials/about.html')
def about():
    slug = 'about-claseh'
    return {
        "about": get_object_or_404(Menu.objects.published(), slug=slug)
    }


@register.inclusion_tag('contact/partials/contact.html')
def contact():
    slug = 'contact'
    return {
        "contact": get_object_or_404(Menu.objects.published(), slug=slug)
    }


@register.inclusion_tag('contact/partials/contactform.html')
def contactform():
    return {
        "contactform": ContactForm,
    }


@register.inclusion_tag('home/partials/services.html')
def services():
    slug = 'services'
    category = get_object_or_404(MenuCategory.objects.active(), slug=slug)
    return {
        "service": category.menus.all()
    }


@register.inclusion_tag('home/partials/webdesign.html')
def webdesign():
    slug = 'web-design'
    category = get_object_or_404(MenuCategory.objects.active(), slug=slug)
    return {
        "webdesigns": category.menus.all()
    }


@register.inclusion_tag("home/partials/menu.html")
def menu():
    return {
        "menus": MenuCategory.objects.active()
    }


@register.inclusion_tag("pages/partials/pagesmenu.html")
def pagesmenu():
    return {
        "menu": Menu.objects.published(),
        "category": MenuCategory.objects.active(),
    }