from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from movieactor import logic
from django.urls import reverse

from .forms import NameForm

movieactor_page = """
<a href="/movieactor/">Go back</a>
"""

def home_view(request):
    return render(request, 'movieactor/homepage.html')

def movieactor_home(request):
    form = NameForm()
    if request.method =='POST':
        form = NameForm(request.POST)
        if form.is_valid():
            #form.save(commit=True)
            name1 = form.cleaned_data['name1']
            name2 = form.cleaned_data['name2']
            #logic.ask(name1, name2)
            if name1 and name2 != None:
                cast1, cast2 = logic.ask(name1, name2)
                matchingActor = logic.compare(cast1, cast2)
                actorFilmography = logic.crossReference(str(matchingActor))
            else:
                raise ValueError("You must put two titles of movies.")
            #names = name1 + " " + name2
            getactorview = (actorFilmography)
            return render(request, 'movieactor/movieactor.html',{
        'form':form, 'getactorview':getactorview, 'name1':name1, 'name2':name2, 'matchingActor':str(matchingActor).strip("\{'}"),
    })
            #return redirect('')
            #for movieJob in getactorview:
                #return HttpResponse(getactorview, content_type="text/plain")
                #for movieRole in movieJob:
                    #return HttpResponse(movieRole)
    else:
        print('ERROR')
    return render(request, 'movieactor/movieactor.html',{
        'form':form,
    })
    

# how the heck will I get my name to display after I hit submit??????