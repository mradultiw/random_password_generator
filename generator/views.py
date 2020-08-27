from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def homepage(requests):
    return render(requests, 'generator/home.html')


def password_page(requests):
    if not 6 <= int(requests.GET.get('length', 6)) <= 14:
        return
    thepassword = __generate_password(requests)
    return render(requests, "generator/password.html", {'password': thepassword})


def about(requests):
    return render(requests, "generator/about.html")


def __generate_password(requests):
    thepassword = []
    characters = [string.ascii_lowercase]
    length = int(requests.GET.get('length', 6))
    uppercase = bool(requests.GET.get('uppercase'))
    number = bool(requests.GET.get('number'))
    special = bool(requests.GET.get('special_char'))
    if uppercase:
        characters.append(string.ascii_uppercase)
    if number:
        characters.append(string.digits)
    if special:
        characters.append("!@#$%&*()")
    for _ in range(int(length * 0.4) + 1):
        thepassword.append(random.choice(characters[0]))
    for _ in range(int(length * 0.2) + 1):
        thepassword.append(random.choice(characters[1 % len(characters)]))
    for _ in range(int(length * 0.2) + 1):
        thepassword.append(random.choice(characters[2 % len(characters)]))
    for _ in range(int(length * 0.2) + 1):
        thepassword.append(random.choice(characters[3 % len(characters)]))
    random.shuffle(thepassword)
    return ''.join(thepassword[:length])
