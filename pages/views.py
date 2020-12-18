from django.shortcuts import render,get_object_or_404
from mentors.models import Mentor
from mentors.choices import district_list, divisions_list, price_choices, category_list

def index(request):
    mentors = Mentor.objects.order_by('-join_date')[:3]

    context = {
        'mentors' : mentors,
        'district_list' : district_list,
        'divisions_list' : divisions_list,
        'price_choices' : price_choices,
        'category' : category_list
    }
    return render(request,'pages/index.html',context)
