from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request):
    return render(request, 'generator/index.html', {'password': 'jhasjhdsjh'})

def password(request):
    password_length = int(request.GET.get('length'))
    uppercase_selected = request.GET.get('uppercase')
    special_selected  = request.GET.get('special')
    numbers_selected = request.GET.get('numbers')
    chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9',]
    special_chars = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password = []
    while len(password) < password_length:
        if numbers_selected:
            chars.extend(nums)
        if special_selected:
            chars.extend(special_chars)
        password.append(random.choice(chars))
    final_password = ''.join(password)



    return render(request, 'generator/generated-password.html', {'final_password': final_password})
